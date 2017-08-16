import psycopg2

def parseProjectFile(filename):
    pList = []
    with open(filename,"r") as projectFile:
        pDict = {}
        for line in projectFile:
            if "~~~" in line:
                pList.append(pDict)
                pDict = {}
            else:
                p = line.split("::")
                pDict[p[0]] = p[-1][:-1]
                if pDict[p[0]] == '':
                    pDict[p[0]] = None

    print(pList)
    return pList

def enterProject(cur, projectDict):
    executeStr = "INSERT INTO projects (title, github_link, demo_link, str_id, main_desc, more_desc, large_image, med_image, tiny_image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cur.execute(executeStr,(projectDict['title'],projectDict['gitLink'],projectDict['demoLink'],projectDict['strID'],projectDict['descMain'],projectDict['descMore'],projectDict['largeImage'],projectDict['medImage'],projectDict['tinyImage']))

def run():
    #conn = psycopg2.connect(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(dbname="resume", user="conzty01")
    cur = conn.cursor()
    cur.execute("DELETE FROM projects;")

    projectList = parseProjectFile("projects.txt")
    for item in projectList:
        enterProject(cur, item)

    conn.commit()

if __name__ == "__main__":
    run()
