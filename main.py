from difflib import get_close_matches
import mysql.connector
def foo(w):
    con=mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )

    cursor=con.cursor()
    query=cursor.execute("SELECT * FROM Dictionary where Expression = '%s' "%w.lower())
    result=cursor.fetchall()
    if result:
        for res in result:
            print(res[1])
            return
    else:
        query = cursor.execute("SELECT * FROM Dictionary where Expression = '%s' " % w.title())
        result = cursor.fetchall()
        if result:
            for res in result:
                print(res[1])
                return


    data=cursor.execute("SELECT Expression FROM Dictionary")
    data=cursor.fetchall()
    lst=list(set([x[0] for x in data]))
    proposiotion = get_close_matches(word, lst, 5, 0.8)
    w=input(f"Maybe you wanted one of there words {proposiotion}? Y or N: ")
    if w.lower()=='y':
        nw=input(f"Choose the word: {proposiotion} ")
        foo(nw.lower())
    else:
        exit()


if __name__ =='__main__':
    word = input("Please enter a word: ")
    foo(word)

