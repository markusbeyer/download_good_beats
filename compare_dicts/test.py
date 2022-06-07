import filecmp
c = filecmp.dircmp("C:\\Users\\Bruce Pearce\\OneDrive\\Desktop\\1", "C:\\Users\\Bruce Pearce\\OneDrive\\Desktop\\2")

def report_recursive(dcmp):
    for name in dcmp.diff_files:
        print("DIFF file %s found in %s and %s" % (name, 
            dcmp.left, dcmp.right))
    for name in dcmp.left_only:
        print("ONLY LEFT file %s found in %s" % (name, dcmp.left))
    for name in dcmp.right_only:
        print("ONLY RIGHT file %s found in %s" % (name, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print(sub_dcmp)

report_recursive(c)
