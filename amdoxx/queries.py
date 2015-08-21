import MySQLdb as mysql
import util
from members import AmMember

class AmQuery():
    def __init__(self):
        self.conn = mysql.connect('localhost', user='am_username', passwd='am_password', db='am')

    def search_email(self, email):
        """Find a member based on their email, or None if email does not exist"""
        email = util.sql_escape(email)
        result = util.fetch_first_or_none(self.conn.cursor(),
                                          "select id, email, first_name, last_name " +
                                          "from am_am_member inner join aminno_member_email " + 
                                          "on am_am_member.id = aminno_member_email.pnum " + 
                                          "where aminno_member_email.email = '" + email + "';")
        return AmMember(self.conn, *result) if result is not None else None

    def search_first_last(self, fname, lname):
        """Find a member based on their first and last name, or None if not exist"""
        fname, lname = tuple(map(lambda s: util.sql_escape(s), [fname, lname]))
        result = util.fetch_first_or_none(self.conn.cursor(),
                                          "select id, email, first_name, last_name " +
                                          "from am_am_member inner join aminno_member_email " + 
                                          "on am_am_member.id = aminno_member_email.pnum " + 
                                          "where am_am_member.first_name = '" + fname + "'" + 
                                          "and am_am_member.last_name = '" + lname + "';")
        return AmMember(self.conn, *result) if result is not None else None
    
        
