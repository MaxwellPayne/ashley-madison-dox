import util

""" TODO: incorporate interests into AmMember
const ATTACHED_FEMALE_SEEKING_MALE = 1;
const ATTACHED_MALE_SEEKING_FEMALE = 2;
const SINGLE_MALE_SEEKING_FEMALE = 3; 
const SINGLE_FEMALE_SEEKING_MALE = 4;
const MALE_SEEKING_MALE = 5;
const FEMALE_SEEKING_FEMALE = 6;
"""

class AmMember():
    def __init__(self, conn, member_id, email="", fname="", lname=""):
        self.cursor = conn.cursor()
        self.member_id, self.email = member_id, email
        self.fname, self.lname = fname, lname

    @property
    def is_complete(self):
        return self.member_id and self.email and self.fname and self.lname

    @property
    def opento(self):
        results = util.fetch_first_or_none(self.cursor,
                                           "select pref_opento " + 
                                           "from am_am_member " + 
                                           "where id = %d;" % self.member_id)
        if results is None:
            raise MemberDNEException()
        return self._get_preference_names(results[0], _opento)

    @property
    def lookingfor(self):
        results = util.fetch_first_or_none(self.cursor,
                                           "select pref_turnsmeon " + 
                                           "from am_am_member " + 
                                           "where id = %d;" % self.member_id)
        if results is None:
            raise MemberDNEException()
        return self._get_preference_names(results[0], _lookingfor)

    @staticmethod
    def _get_preference_names(piped_preferences, preference_dict):
        names = []
        for pref_num in map(int, piped_preferences.rstrip('|').lstrip('|').split('|')):
            if pref_num in preference_dict:
                names.append(preference_dict[pref_num])
            else:
                names.append('<Unknown Preference>')
        return names

    def __str__(self):
        if self.is_complete:
            return '<Member %d with email: %s, fname: %s, lname: %s>' % \
                (self.member_id, self.email, self.fname, self.lname)
        else:
            return '<Member %d with incomplete information>' % self.member_id

    def __repr__(self):
        return str(self)


class MemberDNEException(Exception):
    pass

_opento = {
    1: "Threesome",
    3: "Being Dominant/Master",
    4: "Being Submissive/Slave",
    6: "Bondage",
    7: "Conventional Sex",
    11: "Fetishes",
    14: "Nothing Kinky",
    15: "One-Night Stands",
    17: "Role Playing",
    18: "Sex Talk",
    19: "Spanking",
    21: "Experimenting with Tantric Sex",
    22: "Transvestitism",
    23: "Experimenting with Sex Toys",
    23: "Exploring with Sex Toys",
    26: "Aggressiveness",
    27: "Blindfolding",
    28: "Bubble Bath for 2",
    29: "Cuddling & Hugging",
    30: "Curious - Domination",
    31: "Curious - Submission",
    32: "Dressing Up/Lingerie",
    33: "Erotic Movies",
    34: "Erotic Tickling",
    36: "Extended Foreplay/Teasing",
    37: "Gentleness",
    38: "Good With Your Hands",
    39: "Kissing",
    40: "Light Kinky Fun",
    41: "Likes to be Watched/Exhibitionism",
    42: "Likes to Give Oral Sex",
    43: "Likes to Receive Oral Sex",
    44: "Likes to Go Slow",
    45: "Lots of Stamina",
    46: "Open to Experimentation",
    48: "Sensual Massage",
    49: "Sharing Fantasies",
    50: "Someone I Can Teach",
    51: "Someone Who Can Teach Me",
    52: "You Like to Cross Dress",
}

_lookingfor = {
    1: "A Don Juan",
    4: "Sense of Humor",
    6: "Aggressive/Take Charge Nature",
    9: "Average Sex Drive",
    10: "Confidence",
    11: "Discretion/Secrecy",
    12: "Dislikes Routine",
    14: "Good Personal Hygiene",
    16: "Has a Secret Love Nest",
    17: "High Sex Drive",
    18: "Imagination",
    19: "Likes Routine",
    30: "A Professional/Well Groomed",
    31: "Stylish/Classy",
    32: "Casual Jeans/T-shirt Type",
    33: "Tattoos",
    34: "Body Piercing",
    35: "BBW",
    36: "Full Size Body",
    37: "Muscular/Fit Body",
    38: "Petite Figure",
    39: "Slim to Average Body",
    40: "Tall Height",
    41: "Short Height",
    42: "Long Hair",
    43: "Short Hair",
    44: "Girl Next Door",
    45: "Naughty Girl",
    46: "Bad Boy",
    47: "Boy Next Door",
    48: "Creative and Adventurous",
    49: "Relaxed and Easy Going",
    50: "Hopeless Romantic",
    51: "A Father Figure",
    52: "Not Possessive",
    53: "A Good Listener",
    54: "Good Communicator",
    55: "Disease Free",
    56: "Drug Free",
    57: "Casual/Social Drinker",
    58: "Seeking a Sugar Baby",
    59: "Seeking a Sugar Daddy",
    60: "Natural Breasts",
    61: "Facial Hair",
    62: "Tall, Dark and Handsome",
}
