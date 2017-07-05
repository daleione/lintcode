def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    l = s.split()
    l.reverse()
    ret = ' '.join(l)
    return ret


print reverseWords("")
