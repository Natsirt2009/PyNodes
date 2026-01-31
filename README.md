# PyNodes
A dynamic python node/block renderering and processing library

# How to use
create a folder `data`
for each module you want to create put another folder inside `data`
for each node or block you want put a folder inside your module folder
lastly create a file called `object.xml` inside the node folder.
To add functionality you might want to add an `action.py` file.

The structure should look like this:
```
data
|---module
|   |---node
|   |   |---object.xml
|   |   |---action.py
```

Inside object.xml you can create nodes, types and blocks.  
For a node:
```xml
<node title="<your-title>">
    <input type="<type>" name="<input-name>" />
    <output type="<type>" name="<output-name>" />
    <action name="<name>" />
</node>
```
For a block:
```xml
<block title="<your-title>" output_type="<type>">
    <input type="<type>" name="<input-name>" />
    <action name="<name>" />
</block>
```
For a type:
```xml
<type title="<your-title>">
    <!-- Work in progress -->
</type>
```

