input = LOAD $file USING PigStorage(',') AS $schema

output =FOREACH input
        GENERATE 
            x+$increment as x:int;

