# Lucky Scraper
Uses Beautiful Soup 4 and Requests to download the actual USD to JPY
exchange rate that is available locally in Okinawa, Japan. The data 
is coming from an RSS/Atom feed on the website of a local exchange 
business.

The data is then saved into JSON in the current working directory of 
the program. This data will be reloaded into memory and saved with 
any new data.

## Dependencies

### External Libraries
Beautiful Soup 4 and Requests, see requirements.txt for versions that
have worked in testing.

## Roadmap
I want to use this project as a launching pad to begin learning about
 the myriad data persistence methods available, to eventually be 
connected to a SQL database. I have not set a deadline for this and 
intend to only work on this as time and mood suits.

## Lessons Learned
Assumptions I made
- using a date object is better than using text
- using an RSS feed parser will make this easy
- xml is easy to handle because of the structure

Reflections:
- no tool is always the best for every job
- I don't like RSS/Atom feeds because...
- dealing with XML is a nightmare
- no seriously, can we replace it with JSON?
