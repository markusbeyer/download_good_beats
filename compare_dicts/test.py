import filecmp
c = filecmp.dircmp("C:\\Users\\marku\\OneDrive\\To-Do\\MATRIX\\GitHub\\download_good_beats\\compare_dicts\\1", "C:\\Users\\marku\\OneDrive\\To-Do\\MATRIX\\GitHub\\download_good_beats\\compare_dicts\\2")

#only compares dicts

def report_recursive(dcmp):
    for name in dcmp.diff_files:
        print("DIFF file %s found in %s and %s" % (str(name), 
            str(dcmp.left), str(dcmp.right)))
    for name in dcmp.left_only:
        print("ONLY LEFT file %s found in %s" % (name, dcmp.left))
    for name in dcmp.right_only:
        print("ONLY RIGHT file %s found in %s" % (name, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print(sub_dcmp)

report_recursive(c)
