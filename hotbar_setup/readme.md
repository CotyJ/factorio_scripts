# Hotbar Setup

Simple script to set up the hotbar. Uses Python Mouse package to move the mouse to each hotbar position, click, then click the appropriate item tab, then click on the item.

I made a preset for my common use. Others can be added in the <code>presets</code> folder.

Change which hotbar slot you want an item to be in by modifying the key value. For example, if you want Coal to be in the 1st row of the 2nd column, change the preset of '1-2' to 'coal'.

Not all items are in the <code>items</code> folder, but most commonly used ones are.

Add an item by adding to the items Python file like so:

    "name": ["Name", tab_location, row, col]

"name" should match the name that will be entered in the preset key value.

![Example](https://github.com/CotyJ/factorio_scripts/blob/main/hotbar_setup/factorio_script_preview.gif?raw=true)