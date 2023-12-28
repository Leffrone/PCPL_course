
int min(int a, int b, int c)
{
    int m = a;
    if (b < m) m = b;
    if (c < m) m = c;
    return m;
}
int LD(string word1, int len1, string word2, int len2)
{
    if (len1 == 0) { return len2; }
    if (len2 == 0) { return len1; }

    int substitutionCost = 0;

    if (word1[len1 - 1] != word2[len2 - 1]){ substitutionCost = 1; }
    int deletion = LD(word1, len1 - 1, word2, len2) + 1;
    int insertion = LD(word1, len1, word2, len2 - 1) + 1;
    int substitution = LD(word1, len1 - 1, word2, len2 - 1) + substitutionCost;
    return min(deletion, insertion, substitution);
}

Console.Write(LD("Russia", 5, "America", 6));


