# ashley-madison-dox
A tool you can use to find out if your friends and family are adulterers registered with Ashley Madison. Or rather, one *you could use* if you somehow *happened to have access to* Ashley Madison membership data.  

### Database Setup

Before any of this will work, you need to download and import the Ashley Madison data set into your local MySQL database. Be patient, because this will take a long time. 

1. Download *some data set that looks A LOT like the Ashley Madison hack* (excluding the credit card data if you want; this application does not use it)
2. Unzip every *.dump.gz file
3. For each resulting *.dump file, run `mysql -u root -p --database=am < filename.dump`

You should now have a database named **am** that has the same structure as Ashley Madison's. You could start querying away on your own, but if you want to do anything cool with reasonable query time, you'll need to make some modifications to this database first. 

#### Modifications to database needed:

Re-indexing tables with 30 million+ records takes a long time. To speed up the process dramatically, you may want to temporarily increase the `sort_buffer_size` variable in your my.cnf file. 

##### To speed up search by first and last name:

```SQL
CREATE INDEX name_lookup ON am_am_member (first_name, last_name);
```

##### To enable fast geospatial queries:

```SQL
CREATE TABLE `am_spatial_lookup` (
    `pnum` INT(11) NOT NULL,
    `location` POINT NOT NULL,
    PRIMARY KEY(`pnum`)
    ) ENGINE=MyISAM;

INSERT INTO am_spatial_lookup
    SELECT id, POINT(latitude, longitude)
    FROM am_am_member;

CREATE SPATIAL INDEX location_data_index 
    ON am_spatial_lookup (location);
```

**Note:** this one may take a while, even with a large `sort_buffer_size`. I used a 4G `sort_buffer_size` and it still took about an hour. 