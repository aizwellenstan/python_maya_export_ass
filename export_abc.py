def ExportAbc(selection, start, end, save_name):
    # AbcExport -j "-frameRange 1 120 -dataFormat ogawa -root |locator1 -root |locator2 -file D:/After.Effect.Plugins/test.abc"
    root = ""
    for i in selection:
        root += " -root %s" % (i)

    command = "-frameRange " + str(start) + " " + str(end) +" -uvWrite -worldSpace " + root + " -file " + save_name
    cmds.loadPlugin( 'AbcExport.mll' )
    cmds.AbcExport ( j = command )
