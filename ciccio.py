import maya.cmds as mc

sel = `mc.ls (sl =1)`
for all in sel:
	print all
	# to try esc :wq