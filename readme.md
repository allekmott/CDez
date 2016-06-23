#CDez
C-dez or CD-ez; SQLite-driven command line tool to keep track of physically-organized
CD collection. Specifically, I've been looking to migrate disks from jewel cases to more
archival and easily-accessible CD boxes, in which sleeves are sorted by number. Instead
of having to go through, box by box, in search of a single disc, one would be able to enter
a simple query and know the exact (or most recently known) location.

##Design
The main design centers around two database tables: a list of artists, and a list of cds.
Each artist is paired with its unique numerical identifier, which is then referenced by a
CD entry, containing the artist, cd name, box, and location. The rest is up to simple SQL
queries.

##Quick Start
...or what the tool is designed for--ease of use.
(TBA)