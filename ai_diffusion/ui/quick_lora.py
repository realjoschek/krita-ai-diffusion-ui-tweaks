from __future__ import annotations

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QComboBox,
    QCompleter,
)
from PyQt5.QtCore import Qt, pyqtSignal

from ..style import Style
from ..files import FileFilter
from ..root import root
from ..settings import settings
from .switch import SwitchWidget
from .theme import SignalBlocker
from .style import LoraList


class QuickLoraItem(QWidget):
    """A simplified LoRA selector for the generation tab."""

    changed = pyqtSignal()

    def __init__(self, loras: FileFilter, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self._loras = loras
        self._current_lora_name = ""

        completer = QCompleter(self._loras)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)

        self._select = QComboBox(self)
        self._select.setEditable(True)
        self._select.setModel(self._loras)
        self._select.setCompleter(completer)
        self._select.setMaxVisibleItems(20)
        self._select.setMinimumWidth(150)
        self._select.currentIndexChanged.connect(self._select_lora)

        self._enabled = SwitchWidget(self)
        self._enabled.setChecked(True)
        self._enabled.toggled.connect(self._notify_changed)

        self._strength = QSpinBox(self)
        self._strength.setMinimum(-400)
        self._strength.setMaximum(400)
        self._strength.setSingleStep(5)
        self._strength.setValue(100)
        self._strength.setSuffix("%")
        self._strength.setMinimumWidth(80)
        self._strength.valueChanged.connect(self._notify_changed)

        layout = QHBoxLayout()
        layout.setContentsMargins(4, 2, 4, 2)
        layout.addWidget(self._select, 3)
        layout.addWidget(self._enabled)
        layout.addWidget(self._strength, 1)
        self.setLayout(layout)

    def _notify_changed(self):
        self.changed.emit()

    def _select_lora(self):
        """Handle LoRA selection change."""
        lora_id = self._select.currentData()
        if lora_id and lora_id != self._current_lora_name:
            self._current_lora_name = lora_id
            self._notify_changed()

    @property
    def strength(self):
        return self._strength.value() / 100

    @strength.setter
    def strength(self, value: float):
        value_int = int(value * 100)
        if value_int != self._strength.value():
            self._strength.setValue(value_int)

    @property
    def value(self):
        return dict(
            name=self._current_lora_name,
            strength=self.strength,
            enabled=self._enabled.isChecked(),
        )

    @value.setter
    def value(self, v: dict):
        self._current_lora_name = v["name"]
        with SignalBlocker(self._select):
            # Find and select the LoRA in the combo box
            index = self._select.findData(v["name"])
            if index >= 0:
                self._select.setCurrentIndex(index)
            else:
                # If not found in filtered list, just show the name
                self._select.setEditText(v["name"])
        self.strength = v["strength"]
        self._enabled.setChecked(v.get("enabled", True))


class QuickLoraList(QWidget):
    """A simplified LoRA list widget for the generation tab showing a fixed number of slots."""

    value_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._items: list[QuickLoraItem] = []
        self._style: Style | None = None
        self._loras = FileFilter(root.files.loras)
        self._loras.available_only = True
        self._apply_folder_filter()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(2)

        # Header
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        self._lora_label = QLabel("LoRA", self)
        self._lora_label.setStyleSheet("QLabel { font-weight: bold; }")
        header_layout.addWidget(self._lora_label)

        header_layout.addStretch()
        self._layout.addLayout(header_layout)

        # Items container
        self._item_list = QVBoxLayout()
        self._item_list.setContentsMargins(0, 0, 0, 0)
        self._item_list.setSpacing(2)
        self._layout.addLayout(self._item_list)

        self.setLayout(self._layout)

        # Create the initial number of items based on style
        self._rebuild_items()

    def _apply_folder_filter(self):
        """Apply the folder filter from LoraList settings."""
        folder_filter = LoraList.last_filter
        if folder_filter and folder_filter != "All":
            self._loras.name_prefix = folder_filter
        else:
            self._loras.name_prefix = ""

        # Update existing items to reflect the new filter
        for item in self._items:
            # Store current value
            current_value = item.value.copy() if item.value.get("name") else None
            # The ComboBox model will update automatically
            # But we need to restore the selection if it's still valid
            if current_value and current_value.get("name"):
                item.value = current_value

    def _handle_settings_change(self, name: str, value):
        """Rebuild items when the quick_lora_count setting changes."""
        if name == "quick_lora_count":
            self._rebuild_items()

    def _rebuild_items(self):
        """Rebuild the item list to match the current style's setting."""
        # Re-apply folder filter before rebuilding
        self._apply_folder_filter()

        # Clear existing items
        for item in self._items:
            self._item_list.removeWidget(item)
            item.deleteLater()
        self._items.clear()

        # Create new items based on style's count
        count = self._style.quick_lora_count if self._style else 3
        for _ in range(count):
            item = QuickLoraItem(self._loras, parent=self)
            item.changed.connect(self._update_item)
            self._items.append(item)
            self._item_list.addWidget(item)

        # Reload style if we have one
        if self._style:
            self._load_from_style(self._style)

    def _update_item(self):
        self.value_changed.emit()

    def _load_from_style(self, style: Style):
        """Load LoRAs from style into the fixed number of slots."""
        # Fill available slots with LoRAs from style
        for i, item in enumerate(self._items):
            if i < len(style.loras):
                item.value = style.loras[i]
            else:
                # Empty slot
                item.value = dict(name="", strength=1.0, enabled=True)

    def set_style(self, style: Style):
        """Update the widget to show LoRAs from the given style."""
        # Re-apply folder filter in case it changed
        self._apply_folder_filter()

        # Check if we need to rebuild items due to count change
        needs_rebuild = (
            self._style is None
            or style is None
            or self._style.quick_lora_count != style.quick_lora_count
        )

        self._style = style

        if needs_rebuild:
            self._rebuild_items()
        elif style:
            self._load_from_style(style)

    @property
    def value(self):
        """Get the current LoRA list, filtering out empty slots."""
        return [item.value for item in self._items if item.value.get("name", "")]

    def update_style(self):
        """Update the current style's LoRAs from the widget values."""
        if self._style is not None:
            self._style.loras = self.value
            self._style.save()
