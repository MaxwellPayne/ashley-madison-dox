import MySQLdb as mysql
from queries import AmQuery

_darren_email = 'darren@housecapades.com'

if __name__ == '__main__':
    query = AmQuery()

    print query.search_email('lksdfjasdkljf@lkfjaslk.com')

    # why do these have different member ids?
    print query.search_email(_darren_email)
    print query.search_first_last('darren', 'moregnstern')

    # forget that for now, move on to members
    darren = query.search_email(_darren_email)
    print darren.opento
    print darren.lookingfor
