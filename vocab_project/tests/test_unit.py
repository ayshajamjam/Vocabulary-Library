from vocab_project import (
    word_count,
    retrieve_sentences,
    retrieve_all_words,
    retrieve_all_non_stop_words,
    individual_word_count,
    individual_word_count_non_stop_word,
    top_k_words,
)

# from unittest.mock import patch
import unittest


class Test(unittest.TestCase):
    # My project unit tests

    def test_word_count(self):
        s1 = "I can't make it today. How about tomorrow?"
        s2 = "Broken glass box"
        s3 = "8 chicken nuggets with 3 sides"
        s4 = "merry-go-round"

        self.assertEqual(8, word_count(s1))
        self.assertEqual(3, word_count(s2))
        self.assertEqual(6, word_count(s3))
        self.assertEqual(3, word_count(s4))

    def test_retrieve_sentences(self):
        s1 = ""
        s2 = "She smokes..."
        s3 = "Hi! My name is Khadija."
        s4 = "Sarah, a kind lady, helped me find my way to the mall."
        s5 = "Oh my God! I can't believe it! I'm so surprised to hear this news."

        self.assertEqual([], retrieve_sentences(s1))
        self.assertEqual(['She smokes...'], retrieve_sentences(s2))
        self.assertEqual(['Hi!', 'My name is Khadija.'], retrieve_sentences(s3))
        self.assertEqual(['Sarah, a kind lady, helped me find my way to the mall.'], retrieve_sentences(s4))
        self.assertEqual(
            ["Oh my God!", "I can't believe it!", "I'm so surprised to hear this news."], retrieve_sentences(s5)
        )

    def test_retrieve_words(self):
        s1 = ""
        s2 = "She smokes..."
        s3 = "Hi! My name is Khadija."
        s4 = "Sarah, a kind lady, helped me find my way to the mall."
        s5 = "Oh my God! I can't believe it! I'm so surprised to hear this news."
        s6 = "-$%^ *()"
        s7 = "merry-go-round"

        self.assertEqual([], retrieve_all_words(s1))
        self.assertEqual(['she', 'smokes'], retrieve_all_words(s2))
        self.assertEqual(['hi', 'my', 'name', 'is', 'khadija'], retrieve_all_words(s3))
        self.assertEqual(
            ['sarah', 'a', 'kind', 'lady', 'helped', 'me', 'find', 'my', 'way', 'to', 'the', 'mall'],
            retrieve_all_words(s4),
        )
        self.assertEqual(
            ['oh', 'my', 'god', 'i', "can't", 'believe', 'it', "i'm", 'so', 'surprised', 'to', 'hear', 'this', 'news'],
            retrieve_all_words(s5),
        )
        self.assertEqual([], retrieve_all_words(s1))
        self.assertEqual(['merry', 'go', 'round'], retrieve_all_words(s7))

    def test_retrieve_all_non_stop_words(self):
        s1 = "Oh my God! I can't believe it! I'm so surprised to hear this news."
        s2 = "The the the THE THE"
        s3 = "The New York Times"
        s4 = "Are you surprised 8 people showed up?"

        self.assertEqual(
            ['oh', 'god', "can't", 'believe', "i'm", 'surprised', 'hear', 'news'], retrieve_all_non_stop_words(s1)
        )
        self.assertEqual([], retrieve_all_non_stop_words(s2))
        self.assertEqual(['new', 'york', 'times'], retrieve_all_non_stop_words(s3))
        self.assertEqual(['surprised', '8', 'people', 'showed'], retrieve_all_non_stop_words(s4))

    def test_individual_word_count(self):
        s1 = "I can't make it today. How about tomorrow?"
        s2 = "Surprise, surprise. Funny finding you here."
        s3 = "8 chicken nuggets with 3 sides"
        s4 = "merry-go-round"
        s5 = "The the the THE THE"

        c1 = {'i': 1, "can't": 1, 'make': 1, 'it': 1, 'today': 1, 'how': 1, 'about': 1, 'tomorrow': 1}
        c2 = {'surprise': 2, 'funny': 1, 'finding': 1, 'you': 1, 'here': 1}
        c3 = {'8': 1, 'chicken': 1, 'nuggets': 1, 'with': 1, '3': 1, 'sides': 1}
        c4 = {'merry': 1, 'go': 1, 'round': 1}
        c5 = {'the': 5}

        self.assertEqual(c1, individual_word_count(s1))
        self.assertEqual(c2, individual_word_count(s2))
        self.assertEqual(c3, individual_word_count(s3))
        self.assertEqual(c4, individual_word_count(s4))
        self.assertEqual(c5, individual_word_count(s5))

    def test_individual_word_count_non_stop_word(self):
        s1 = "Oh my God! I can't believe it! I'm so surprised to hear this news."
        s2 = "The the the THE THE"
        s3 = "The New York Times"
        s4 = "Are you surprised 8 people showed up?"

        c1 = {'oh': 1, 'god': 1, "can't": 1, 'believe': 1, "i'm": 1, 'surprised': 1, 'hear': 1, 'news': 1}
        c2 = {}
        c3 = {'new': 1, 'york': 1, 'times': 1}
        c4 = {'surprised': 1, '8': 1, 'people': 1, 'showed': 1}

        self.assertEqual(c1, individual_word_count_non_stop_word(s1))
        self.assertEqual(c2, individual_word_count_non_stop_word(s2))
        self.assertEqual(c3, individual_word_count_non_stop_word(s3))
        self.assertEqual(c4, individual_word_count_non_stop_word(s4))

    def test_top_k_words(self):
        s1 = "On offering to help the blind man, the man who then stole his car, had not, at that precise moment, had any evil intention, quite the contrary, what he did was nothing more than obey those feelings of generosity and altruism which, as everyone knows, are the two best traits of human nature and to be found in much more hardened criminals than this one, a simple car-thief without any hope of advancing in his profession, exploited by the real owners of this enterprise, for it is they who take advantage of the needs of the poor."
        s2 = "My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges."
        s3 = "The French are certainly misunderstood: — but whether the fault is theirs, in not sufficiently explaining themselves, or speaking with that exact limitation and precision which one would expect on a point of such importance, and which, moreover, is so likely to be contested by us — or whether the fault may not be altogether on our side, in not understanding their language always so critically as to know “what they would be at” — I shall not decide; but ‘tis evident to me, when they affirm, “That they who have seen Paris, have seen every thing,” they must mean to speak of those who have seen it by day-light."
        s4 = "All I know is that I stood spellbound in his high-ceilinged studio room, with its north-facing windows in front of the heavy mahogany bureau at which Michael said he no longer worked because the room was so cold, even in midsummer; and that, while we talked of the difficulty of heating old houses, a strange feeling came upon me, as if it were not he who had abandoned that place of work but I, as if the spectacles cases, letters and writing materials that had evidently lain untouched for months in the soft north light had once been my spectacle cases, my letters and my writing materials."

        e1 = "The the the THE THE"
        e2 = "Scorpions lay in the sun, sizzling."

        self.assertEqual([('man', 2), ('car', 2), ('offering', 1)], top_k_words(s1, 3))
        self.assertEqual(
            [('warmth', 2), ('midges', 2), ('photogenic', 1), ('mother', 1), ('died', 1)], top_k_words(s2, 5)
        )
        self.assertEqual([('seen', 3), ('whether', 2)], top_k_words(s3, 2))
        self.assertEqual([('room', 2), ('north', 2), ('cases', 2), ('letters', 2)], top_k_words(s4, 4))

        self.assertRaises(ValueError, top_k_words, e1, 1)
        self.assertRaises(ValueError, top_k_words, e1, 3)
        self.assertRaises(ValueError, top_k_words, e2, 10)

    # def test_get_definition(self):

    #     word = "friend"
    #     def_word = "someone who hates your"

    #     self.assertNotEqual(def_word, get_definition(word))


# if __name__ == '__main__':
#     unittest.main()
