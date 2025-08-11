import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QTreeWidget, QTreeWidgetItem, QPushButton, 
                             QInputDialog, QMessageBox, QLabel, QTextEdit)
from PySide6.QtCore import Qt
from family_member import Family, FamilyMember
from secret_santa import secret_santa_assign, is_valid_assignment

class SecretSantaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.families = []
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Secret Santa Organizer')
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create tree widget for families and members
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel('Families and Members')
        self.tree.setColumnCount(1)
        layout.addWidget(self.tree)
        
        # Create button layout
        button_layout = QHBoxLayout()
        
        # Family management buttons
        self.add_family_btn = QPushButton('Add Family')
        self.add_family_btn.clicked.connect(self.add_family)
        button_layout.addWidget(self.add_family_btn)
        
        self.remove_family_btn = QPushButton('Remove Family')
        self.remove_family_btn.clicked.connect(self.remove_family)
        button_layout.addWidget(self.remove_family_btn)
        
        # Member management buttons
        self.add_member_btn = QPushButton('Add Member')
        self.add_member_btn.clicked.connect(self.add_member)
        button_layout.addWidget(self.add_member_btn)
        
        self.remove_member_btn = QPushButton('Remove Member')
        self.remove_member_btn.clicked.connect(self.remove_member)
        button_layout.addWidget(self.remove_member_btn)
        
        layout.addLayout(button_layout)
        
        # Secret Santa button
        self.run_secret_santa_btn = QPushButton('Run Secret Santa!')
        self.run_secret_santa_btn.clicked.connect(self.run_secret_santa)
        self.run_secret_santa_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; }")
        layout.addWidget(self.run_secret_santa_btn)
        
        # Results display
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setMaximumHeight(200)
        layout.addWidget(QLabel('Secret Santa Results:'))
        layout.addWidget(self.results_text)
        
        # Load initial data
        self.load_initial_data()
        
    def load_initial_data(self):
        """Load the initial families from the test data"""
        # Create families based on the test data
        tyler_family = Family("Tyler")
        tyler_family.add_member_by_name("Brent", "Tyler")
        tyler_family.add_member_by_name("Hayley", "Tyler")
        
        hays_family = Family("Hays")
        hays_family.add_member_by_name("Harrison", "Hays")
        hays_family.add_member_by_name("Vika", "Hays")
        hays_family.add_member_by_name("Ksenia", "Hays")
        hays_family.add_member_by_name("Ellie", "Hays")
        hays_family.add_member_by_name("Sasha", "Hays")
        hays_family.add_member_by_name("Vincent", "Hays")
        
        hitzeroth_family = Family("Hitzeroth")
        hitzeroth_family.add_member_by_name("Matt", "Hitzeroth")
        hitzeroth_family.add_member_by_name("Heather", "Hitzeroth")
        hitzeroth_family.add_member_by_name("Georgie", "Hitzeroth")
        hitzeroth_family.add_member_by_name("Olivia", "Hitzeroth")
        hitzeroth_family.add_member_by_name("Miles", "Hitzeroth")
        hitzeroth_family.add_member_by_name("Jack", "Hitzeroth")
        
        hays2_family = Family("Hays2")
        hays2_family.add_member_by_name("Hunter", "Hays")
        hays2_family.add_member_by_name("Sarah", "Hays")
        hays2_family.add_member_by_name("Knox", "Hays")
        hays2_family.add_member_by_name("Emet", "Hays")
        hays2_family.add_member_by_name("Jane", "Hays")
        hays2_family.add_member_by_name("Hazel", "Hays")
        
        hays3_family = Family("Hays3")
        hays3_family.add_member_by_name("Hal", "Hays")
        hays3_family.add_member_by_name("Cecilie", "Hays")
        
        self.families = [tyler_family, hays_family, hitzeroth_family, hays2_family, hays3_family]
        self.update_tree()
        
    def update_tree(self):
        """Update the tree widget with current families and members"""
        self.tree.clear()
        
        for family in self.families:
            family_item = QTreeWidgetItem(self.tree)
            family_item.setText(0, f"{family.family_name} ({family.get_member_count()} members)")
            family_item.setData(0, Qt.UserRole, family)
            
            for member in family.get_members():
                member_item = QTreeWidgetItem(family_item)
                member_item.setText(0, member.get_full_name())
                member_item.setData(0, Qt.UserRole, member)
        
        self.tree.expandAll()
        
    def add_family(self):
        """Add a new family"""
        name, ok = QInputDialog.getText(self, 'Add Family', 'Enter family name:')
        if ok and name.strip():
            family = Family(name.strip())
            self.families.append(family)
            self.update_tree()
            
    def remove_family(self):
        """Remove selected family"""
        current_item = self.tree.currentItem()
        if current_item and current_item.parent() is None:  # Family item
            family = current_item.data(0, Qt.UserRole)
            reply = QMessageBox.question(self, 'Remove Family', 
                                       f'Are you sure you want to remove the {family.family_name} family?',
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.families.remove(family)
                self.update_tree()
        else:
            QMessageBox.information(self, 'Selection Error', 'Please select a family to remove.')
            
    def add_member(self):
        """Add a new member to selected family"""
        current_item = self.tree.currentItem()
        if current_item and current_item.parent() is None:  # Family item
            family = current_item.data(0, Qt.UserRole)
            first_name, ok1 = QInputDialog.getText(self, 'Add Member', 'Enter first name:')
            if ok1 and first_name.strip():
                last_name, ok2 = QInputDialog.getText(self, 'Add Member', 'Enter last name:')
                if ok2 and last_name.strip():
                    family.add_member_by_name(first_name.strip(), last_name.strip())
                    self.update_tree()
        else:
            QMessageBox.information(self, 'Selection Error', 'Please select a family to add a member to.')
            
    def remove_member(self):
        """Remove selected member"""
        current_item = self.tree.currentItem()
        if current_item and current_item.parent() is not None:  # Member item
            member = current_item.data(0, Qt.UserRole)
            family = current_item.parent().data(0, Qt.UserRole)
            reply = QMessageBox.question(self, 'Remove Member', 
                                       f'Are you sure you want to remove {member.get_full_name()}?',
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                family.remove_member(member)
                self.update_tree()
        else:
            QMessageBox.information(self, 'Selection Error', 'Please select a member to remove.')
            
    def run_secret_santa(self):
        """Run Secret Santa assignment and display results"""
        if len(self.families) < 2:
            QMessageBox.warning(self, 'Not Enough Families', 'You need at least 2 families to run Secret Santa.')
            return
            
        total_members = sum(family.get_member_count() for family in self.families)
        if total_members < 2:
            QMessageBox.warning(self, 'Not Enough Members', 'You need at least 2 members to run Secret Santa.')
            return
            
        assignment = secret_santa_assign(self.families)
        
        if assignment is None:
            self.results_text.setText("No valid Secret Santa assignment could be found.\n\n"
                                    "This might happen if:\n"
                                    "- There are too few families\n"
                                    "- Family sizes are too uneven\n"
                                    "- Try adding more families or members")
        else:
            results = "🎄 Secret Santa Assignments 🎄\n\n"
            for giver, receiver in assignment.items():
                results += f"🎁 {giver.get_full_name()} → {receiver.get_full_name()}\n"
            
            if is_valid_assignment(assignment, self.families):
                results += "\n✅ Assignment is valid!"
            else:
                results += "\n❌ Assignment is INVALID!"
                
            self.results_text.setText(results)

def main():
    app = QApplication(sys.argv)
    
    # Apply dark stylesheet
    dark_stylesheet = """
    QMainWindow {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
        font-size: 12px;
    }
    
    QTreeWidget {
        background-color: #3c3c3c;
        border: 1px solid #555555;
        border-radius: 4px;
        color: #ffffff;
        selection-background-color: #4a90e2;
        alternate-background-color: #404040;
    }
    
    QTreeWidget::item {
        padding: 4px;
        border: none;
    }
    
    QTreeWidget::item:selected {
        background-color: #4a90e2;
        color: #ffffff;
    }
    
    QTreeWidget::item:hover {
        background-color: #404040;
    }
    
    QPushButton {
        background-color: #404040;
        border: 1px solid #555555;
        border-radius: 4px;
        color: #ffffff;
        padding: 8px 16px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #505050;
        border-color: #666666;
    }
    
    QPushButton:pressed {
        background-color: #303030;
    }
    
    QPushButton:disabled {
        background-color: #2a2a2a;
        color: #666666;
        border-color: #444444;
    }
    
    QTextEdit {
        background-color: #3c3c3c;
        border: 1px solid #555555;
        border-radius: 4px;
        color: #ffffff;
        padding: 8px;
    }
    
    QLabel {
        color: #ffffff;
        font-weight: bold;
    }
    
    QInputDialog {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    
    QMessageBox {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    
    QMessageBox QPushButton {
        min-width: 80px;
        min-height: 25px;
    }
    
    QScrollBar:vertical {
        background-color: #3c3c3c;
        width: 12px;
        border-radius: 6px;
    }
    
    QScrollBar::handle:vertical {
        background-color: #555555;
        border-radius: 6px;
        min-height: 20px;
    }
    
    QScrollBar::handle:vertical:hover {
        background-color: #666666;
    }
    
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    
    QScrollBar:horizontal {
        background-color: #3c3c3c;
        height: 12px;
        border-radius: 6px;
    }
    
    QScrollBar::handle:horizontal {
        background-color: #555555;
        border-radius: 6px;
        min-width: 20px;
    }
    
    QScrollBar::handle:horizontal:hover {
        background-color: #666666;
    }
    
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0px;
    }
    """
    
    app.setStyleSheet(dark_stylesheet)
    
    window = SecretSantaUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
