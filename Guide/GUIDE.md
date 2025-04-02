1. https://docs.blender.org/api/current/info_quickstart.html
2. https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
3. https://docs.blender.org/api/current/bpy.ops.html

4. Python Class Stuffs
    - Calling Member Functions
    ```py
    class REY_Nodes_Appender:
        def load_rey_node_groups():
            print("Loaded REY_Nodes from .blend file")

        @classmethod
        def register(self):
            self.load_rey_node_groups()
            print("✅ load_rey_node_groups() has been called!")
    ```
    
    - gdsg

5. Blender Python
    - use the `dir(bpy.ops)` command
        - I used it a lot to get to know the functions and member objects from DAY-1

6. You should kinda have the version of the python that blender has 💁‍♀️
    - and then do `pip install bpy`
    - e.g.
        - as of Blender4.4.
        - Python officially Stable Ships 3.13.x
        - but Blender4.4. uses Python 3.11
        - `bpy` can't work with anything higher 