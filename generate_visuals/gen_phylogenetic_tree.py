from ete3 import Tree, NodeStyle, TreeStyle
t = Tree( "(((f ,e ),(h ,g )),((d ,c ),(b ,a )));" )

# Basic tree style
ts = TreeStyle()
ts.show_leaf_name = True
ts.branch_vertical_margin = 10
# Draws nodes as small red spheres of diameter equal to 10 pixels
nstyle = NodeStyle()

nstyle["shape"] = "sphere"
nstyle["size"] = 2
nstyle["fgcolor"] = "darkred"

# Gray dashed branch lines
nstyle["hz_line_type"] = 1
nstyle["hz_line_color"] = "#cccccc"

# Applies the same static style to all nodes in the tree. Note that,
# if "nstyle" is modified, changes will affect to all nodes
for n in t.traverse():
   n.set_style(nstyle)

#t.show(tree_style=ts)
t.render("mytree.png", dpi=300)
