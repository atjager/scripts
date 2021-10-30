# convertToImportable
To create MySQL importable format from the following (tab separeted) structure:

```
id	hely	tipus	ipcim
1	T403	asztali	192.168.2.1
2	T212	asztali	192.168.2.2
3	T302	asztali	192.168.2.3
```

Then it'll look like this:
```
INSERT INTO gep(id,hely,tipus,ipcim) VALUES ('1','T403','asztali','192.168.2.1');
INSERT INTO gep(id,hely,tipus,ipcim) VALUES ('2','T212','asztali','192.168.2.2');
INSERT INTO gep(id,hely,tipus,ipcim) VALUES ('3','T302','asztali','192.168.2.3');
```

# Usage
- First cli argument: path to file
- Second command line argument: path to output file
- Third cli argument: table name

```
python3 convertToImportable.py path-to-file\filename.txt path-to-output-file\filename.sql tablename
```
