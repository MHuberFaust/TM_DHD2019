def queryreqDNBtitel(query):
    '''sends a cql-query to SRU-API of the DNB

    Args:
        cqlquery(str):CQL-Query

    Returns:



    ToDo: parse response for <datafield tag="100"><subfield code="0">http://d-nb.info/gnd/XXXXXXX</>
    '''

    baseurl = 'https://services.dnb.de/sru/accessToken~c62882b88ff75264bef6a92ba898f591/dnb'
    url = baseurl
    data = requests.get(url, auth=('huber87michael@gmail.com','BW8ybZba'), params={'version':'1.1', 'operation': 'searchRetrieve','query':query,'recordSchema':'MARC21-xml'})
    #print(data.headers)
    #print(data.url)
    #print(data.text)


    ##for marc21-xml
    xmletree= etree.fromstring(data.content)


    datafieldList = xmletree.xpath("//ns:datafield[@tag='100']/ns:subfield[@code='0']", namespaces={"ns":"http://www.loc.gov/MARC21/slim"})
    if datafieldList:
        dataList =[]
        for item in datafieldList:
            #print(item)
            text= item.text
            split = text.split('http://d-nb.info/gnd/')
            if len(split)==2:
                #print(split)
                dataList.append(split[1])
        print(dataList)
        return (dataList)
    else:
        print('no result for ', query)



def queryreqDNBperson(query):
    '''sends a cql-query to SRU-API of the DNB

    Args:
        cqlquery(str):CQL-Query

    Returns:



    '''


    baseurl = 'https://services.dnb.de/sru/accessToken~c62882b88ff75264bef6a92ba898f591/authorities'
    url = baseurl
    data = requests.get(url, auth=('huber87michael@gmail.com','BW8ybZba'), params={'version':'1.1', 'operation': 'searchRetrieve','query':query,'recordSchema':'MARC21-xml'})
    print(data.headers)
    print(data.url)
    print(data.text)



def createCQLQ(title, person):
    '''
    ToDo: strip whitespace
    '''
    print('TIT=',title+' and PER=',person)
    return 'TIT=',title+' and PER=',person

