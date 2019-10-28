# coding: utf-8
from PyQt4.QtCore import QFileInfo
from qgis.core import QgsProject
from qgis.utils import iface

# Get the project instance
project = QgsProject.instance()

# Get layer tree
print(project.layerTreeRoot())  # QgsLayerTreeGroup

# Print the current project file name (might be empty in case no projects have been loaded)
print(project.fileName())

# Store values
project.writeEntry("myplugin", "mytext", "hello world")
project.writeEntry("myplugin", "myint", 10)
project.writeEntry("myplugin", "mydouble", 0.01)
project.writeEntry("myplugin", "mybool", True)

# Read values
mytext = project.readEntry("myplugin", "mytext", "default text")[0]
myint = project.readNumEntry("myplugin", "myint", 123)[0]

# Read values list
print(project.readListEntry('Scales', 'ScalesList'))


# Function to check if project already read
def loaded():
    print('loaded')

# Combined with previous function, check when the project already read
iface.projectRead.connect(loaded)

# Load another project
project.read(QFileInfo('/home/user/projects/my_other_qgis_project.qgs'))

# Save the project to the same
project.write()
# ... or to a new file
project.write(QFileInfo('/home/user/projects/my_new_qgis_project.qgs'))

# Start a new empty project
iface.newProject()
