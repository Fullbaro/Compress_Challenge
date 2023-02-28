A compression challenge inspired by the Silicon Valley series. The goal was to write a compression algorithm where no external libraries could be imported and the use of any internet or other help was prohibited.
My approach was to find the most ideal length of the most frequently occurring strings in a text and then replace them with a single random character from the UTF-8 character table. I saved the swaps in a dictionary at the beginning of the file, so that I can restore the file.
