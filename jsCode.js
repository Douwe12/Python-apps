function disemvowel(str) {
    vowels = ['a', 'u', 'i', 'o', 'e'];
    final_str = '';
    for (let char of str) {
      if (!vowels.includes(char.toLowerCase()))
        final_str += char;
    }
    return final_str;
  }