from audioop import error

from connections.connection import createConnection

class MysqlConnectivity:


    def createTables(self,tname,*n):
        try:
            conn=createConnection()
            curs=conn.cursor()
        except(Exception,error):
            print("Something went wrong during Connection establish")

        t=tuple(n[0])
        strs=""
        for i in t:
            strs=strs+i+', '

        strs=strs[:len(strs)-2]
        try:

            st=f" CREATE TABLE  {tname} ({strs}); "
            print(st)
            curs.execute(st)
            # curs.execute(f"create table {tname} ({strs});")
            # print((f"create table {tname} ({strs})"))
        except(Exception,error)as err:
            print(err)
        else:
            print("So far so good your table has been created successfully ")
        finally:
            conn.close()


    def insertData(self,tn,*n):
        try:
            t = tuple(n[0])
            conn = createConnection()
            curs = conn.cursor()
            curs.execute(f'insert into {tn} value {t}')
        except(Exception,error) as e:
            print(e)
        else:
            conn.commit()
            print("Data has been inserted successfully into the table ")
        finally:

            conn.close()
            curs.close()




    def read(self,tname,take):
        conn=createConnection()
        curs=conn.cursor()
        sts=f"select * from {tname};"
        try:
            curs.execute(sts)
            fields = list(map(lambda x: x[0], curs.description))
            data=curs.fetchall()
            for value in data:
                cout=0
                for j in fields:
                    print(f"{j} :{value[cout]} ||",end=" ")
                    cout+=1
                print()

        except(Exception,error) as e:
            print(e)
        finally:
            conn.close()
            curs.close()


    def delete(self,tname,name,keys):
        try:
            conn=createConnection()
            curs=conn.cursor()
            sts=f"delete from {tname} where {name}={keys};"
            curs.execute(sts)
        except(Exception,error) as e:
            print(e)
        else:
            print("The data has been successfully deleted.")
        finally:
            conn.commit()
            conn.close()
            curs.close()

    def dropTable(self,tname):
        try:
            conn = createConnection()
            curs = conn.cursor()
            sts = f"drop table {tname}"
            curs.execute(sts)
        except(Exception,error) as e:
            print(e)
        else:
            print("Table has been successfully droped from the database ")
        finally:
            conn.commit()
            conn.close()
            curs.close()



    def descriptions(self,tname):
        conn= createConnection()
        curs = conn.cursor()
        try:
            curs.execute(f'select * from {tname}')
            fields = list(map(lambda x: x[0], curs.description))
            return fields
        except(Exception,error) as e:
            print(e)
        finally:
            conn.close()
            curs.close()











