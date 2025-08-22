---
source_url: https://cascadeur.com/python-api/_generate/csc.app.ProjectLoader.html
html_file: ea75dc1516040730ff89071670068ab6.html
module: csc.app.ProjectLoader
---

# csc.app.ProjectLoader 

ProjectLoader class Provides methods to load domain scene. Methods __init__ (*args, **kwargs) load_from (arg0, arg1) Minimal Load. Minimal Load. This method doesn't load selection groups, control picker and etc.
Better use data_source_manager's load_scene method.
Example:
csc.app.ProjectLoader.load_from(file_path, scene)