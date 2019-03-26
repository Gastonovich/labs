import os
import math

def count_freq(chars):
    freq = {}
    total = sum(chars.values())
    for char in chars.keys():
        freq[char] = chars[char] * 1. / total
    
    return freq


def count_amount(string):
    chars = {}
    print(string)
    for char in string:
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    
    return chars


def count_entropy(freq):
    entropy = 0
    for char in freq:
        entropy -= freq[char] * math.log(freq[char], 2)

    return entropy


def get_results(string):
    chars = count_amount(string)
    freq = count_freq(chars)
    entropy = count_entropy(freq)

    return chars, freq, entropy


def visualize_sep(chars, freq):
    order = sorted([*chars])
    
    df1 = pd.DataFrame.from_dict(chars, orient='index')
    df1 = df1.reindex(order)
    ax = df1.plot(kind='bar')
    ax.legend(['quantity of chars'])
    plt.show()

    df2 = pd.DataFrame.from_dict(freq, orient='index')
    df2 = df2.reindex(order)
    ax = df2.plot(kind='bar', color='green')
    ax.legend(['frequency of chars'])
    plt.show()


def process_file(file, name):
    string = file.read()
    chars, freq, entropy = get_results(string)
    print('Chars amounts in %s' % name)
    keys = [*chars]
    keys.sort()
    for key in keys:
        print('%s: %i' % (key, chars[key]))
    print

    print('Chars frequency in %s' % name)
    for key in keys:
        print('%s: %f' % (key, freq[key]))

    print('Entropy: %f' % entropy)
    print('Quantity of information: %f' % (entropy * sum(chars.values()) / 8))
    visualize_sep(chars, freq)

    return entropy * sum(chars.values()) / 8

