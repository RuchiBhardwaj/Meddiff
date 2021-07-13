def group_by_owners(filename):
    fi = filename.values()
    s = set(fi)
    result={}
    ownerList = list(s)
    for owner in ownerList:
        lis=[]
        for file in filename:
            if owner == filename[file]:
                lis.append(file)
        result[owner]=lis
    return result


filename= {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(filename))