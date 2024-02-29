# Removed the __future__ import and sys.reload as they are unnecessary/redundant in Python 3
from . import lang_EU

class Num2Word_AR(lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        max_value = 3 + 3 * len(high)  # Renamed 'max' to 'max_value' to avoid shadowing built-in function
        for word, n in zip(high, range(max_value, 3, -3)):
            self.cards[10 ** n] = word + "مليون"

    def setup(self):
        self.negword = " سالب "
        self.pointword = "."
        self.errmsg_nornum = "فقط الارقام يمكن تحويلها الي كلمات."
        self.exclude_title = ["و", ".", "و"]

        self.mid_numwords = [(1000, "ألف"), (100, "مائة"),
                             (1000000,"مليون"),
                             (1000000000,"مليار"),
                             (1000000000000, "بليون"),
                             (1000000000000000, "بليار"),
                             (1000000000000000000, "تريليون"),
                             (1000000000000000000000, "تريليار"),
                             (1000000000000000000000000, "كتريلليون"),
                             (1000000000000000000000000000, "كتريليار"),
                             (1000000000000000000000000000000, "سنكلليون"),
                             (1000000000000000000000000000000000, "سنكليار"),
                             (1000000000000000000000000000000000000, "سيزليون"),
                             (1000000000000000000000000000000000000000, "سيزليار"),
                             (1000000000000000000000000000000000000000000, "سيتيليون"),
                             (1000000000000000000000000000000000000000000000, "سيتليار"),
                             (1000000000000000000000000000000000000000000000000, "ويتيليون"),
                             (1000000000000000000000000000000000000000000000000000, "ويتيليار"),
                             (1000000000000000000000000000000000000000000000000000000, "نفيليون"),
                             (1000000000000000000000000000000000000000000000000000000000, "نيفليار"),
                             (1000000000000000000000000000000000000000000000000000000000000, "ديسليون"),
                             (1000000000000000000000000000000000000000000000000000000000000000, "ديسليار"),


                             (90, "تسعون"), (80, "ثمانون"), (70, "سبعون"),
                             (60, "ستون"), (50, "خمسون"), (40, "أربعون"),
                             (30, "ثلاثين")]
        self.low_numwords = ["عشرون", "تسعة عشر", "ثمانية عشر", "سبعة عشر",
                             "ستة عشر", "خمسة عشر", "أربعة عشر", "ثلاثة عشر",
                             "اثنا عشر", "احدا عشر", "عشرة", "تسعة", "ثمانية",
                             "سبعة", "ستة", "خمسة", "أربعة", "ثلاثة", "اثنان",
                             "واحد", "صفر"]
        self.ords = {"one": "first",
                     "two": "second",
                     "three": "third",
                     "five": "fifth",
                     "eight": "eighth",
                     "nine": "ninth",
                     "twelve": "twelfth"}
    

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split(" و ")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie"
            lastword += "th"
        lastwords[-1] = self.title(lastword)
        outwords[-1] = " و ".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, longval=True):
        if not (val // 100) % 10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt="hundred", jointxt="and", longval=longval)

    def to_currency(self, val, longval=True):
        return self.to_splitnum(val, hightxt="dollar/s", lowtxt="cent/s", jointxt="and", longval=longval, cents=True)

# Example of how you might instantiate and use this class
n2w = Num2Word_AR()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num
to_year = n2w.to_year

def main():
    for val in [1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
                180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
                8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
                -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)  # Ensure the Num2Word_AR class has a test method

    n2w.test(
        1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730)
    
    for val in [1, 120, 1000, 1120, 1800, 1976, 2000, 2010, 2099, 2171]:
        print(f"{val} is {n2w.to_currency(val)}")
        print(f"{val} is {n2w.to_year(val)}")

if __name__ == "__main__":
    main()
