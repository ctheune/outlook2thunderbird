# Outlook CSV to Thunderbird CSV address book converter #

Convert Outlook CSV address book files (currently German locale headers
expected) to Thunderbird CSV files for easy import.

### What is this repository for? ###

A Python-based utility to convert Outlook address CSV files to Thunderbird.

It currently was made as a one off for converting a relatives addressbook
and only picks up a number of fields but makes sure they end up properly
in Thunderbird (or adds them in a semi-structured way to the Notes field).

Feel free to provide PRs for extensions.

### How do I get set up? ###

* Export from Outlook to CSV file (Windows Encoding)
* ./bootstrap.sh
* mv <original outlook file> outlook.csv
* bin/python convert.py

Then import to a new addressbook in Thunderbird.

### Contribution guidelines ###

Write a PR and or an issue.

### Who do I talk to? ###

Feel free to talk to me by just writing an issue here on Bitbucket in the tracker.

