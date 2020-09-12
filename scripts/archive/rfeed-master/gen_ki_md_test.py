'''Test file for genKnownIssuesMD.py'''

import gen_ki_md as gki

def test_build_include():
    '''Test to see if the include build works by testing length'''
    testdata = ['This issue applies to all supported releases.', 
        'Operator',
        '160b8111-eab0-ea11-a812-000d3a5465d8',
        'A new network interface cannot be added to a VM that is in a running state.',
        'sranthar@microsoft.com',
        "nan",
        "nan",
        'Network',
        'azs-1041',
        'Ready',
        'Common',
        'Stop the virtual machine before adding/removing a network interface.',
        'Network interface: Primary Network Interface',
        "nan"]
    testmd = gki.build_include(testdata)
    assert len(testmd) == 405

def test_get_data_from_csv():
    '''Test to see if the sort and transform works correcty.'''
    testcsv = r"C:\git\mb\azs-modular-poc\data\reports\creeb_validator.csv"
    testlist =  gki.get_data_from_csv(testcsv)
    test_item = testlist[0][1]
    valid_item = "azs-1046"
    assert test_item == valid_item