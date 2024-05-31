# QGIS-Plugin-MTDI
### Plugin Builder Results

Congratulations! You just built a plugin for QGIS!  
  

Your plugin **RouteNetwork** was created in:  
  **C:/...QGIS\_Plugins\\route\_network**

Your QGIS plugin directory is located at:  
  **C:/...QGIS/QGIS3/profiles/default/python/plugins**

### What's Next

1.  If resources.py is not present in your plugin directory, compile the resources file using pyrcc5 (simply use **pb\_tool** or **make** if you have automake)
2.  Optionally, test the generated sources using **make test** (or run tests from your IDE)
3.  Copy the entire directory containing your new plugin to the QGIS plugin directory (see Notes below)
4.  Test the plugin by enabling it in the QGIS plugin manager
5.  Customize it by editing the implementation file **route\_network.py**
6.  Create your own custom icon, replacing the default **icon.png**
7.  Modify your user interface by opening **route\_network\_dialog\_base.ui** in Qt Designer

Notes:

*   You can use **pb\_tool** to compile, deploy, and manage your plugin. Tweak the _pb\_tool.cfg_ file included with your plugin as you add files. Install **pb\_tool** using _pip_ or _easy\_install_. See **http://loc8.cc/pb\_tool** for more information.
*   You can also use the **Makefile** to compile and deploy when you make changes. This requires GNU make (gmake). The Makefile is ready to use, however you will have to edit it to add addional Python source files, dialogs, and translations.

For information on writing PyQGIS code, see **http://loc8.cc/pyqgis\_resources** for a list of resources.

©2011-2019 GeoApt LLC - geoapt.com
