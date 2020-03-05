
import glob
from concurrent.futures.thread import ThreadPoolExecutor
from functools import lru_cache
from itertools import chain
from timeit import timeit
import subprocess as sbp
from xml.dom.minidom import parseString
from os import cpu_count



def get_svn_info(filepath):
    value = sbp.check_output(["svn", "info", "--xml", filepath])
    dom = parseString(value)
    entry = dom.getElementsByTagName("entry").item(0)
    revision = entry.getAttribute("revision")
    commit = dom.getElementsByTagName("commit").item(0)
    file_revision = commit.getAttribute("revision")
    date = commit.getElementsByTagName("date").item(0).firstChild.nodeValue
    author = commit.getElementsByTagName("author").item(0).firstChild.nodeValue

    return revision, file_revision, date, author


def baseline():
    return {
        filepath: get_svn_info(filepath)
        for filepath in glob.glob("root/**/*.txt", recursive=True)
    }


def get_revision(filepath):
    return filepath, get_svn_info(filepath)


def fast_impl():
    # Implement your faster implementation of baseline
    # Requirement:
    #    - shall be compatible with Python 3.7
    #    - shall return a dict equal to the baseline dict
    #    - get_svn_info shall not be modified
    with ThreadPoolExecutor(max_workers=(cpu_count() + 4)) as executor:
       results = dict(executor.map(get_revision, glob.glob("root/**/*.txt", recursive=True)))
    return results



def are_dict_equals(expected, result):
    return all(
        key in expected and key in result and expected[key] == result[key]
        for key in set(chain(expected.keys(), result.keys()))
    )


if __name__ == '__main__':
    if are_dict_equals(baseline(), fast_impl()):
        print("Your implementation is correct")
    else:
        print("Your implementation is incorrect")
        exit(1)
    print("It took ", timeit(fast_impl, number=10), "s to run 10 times")

