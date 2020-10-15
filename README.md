# README

Python + migration = Pygration

PygrationはDBのバージョン管理をします。  
フレームワークはいらないけどDBは使いたいしバージョン管理もしたいときに使います。

Pygration manages the version of the DB.
It is used when "I don't need a framework, but I want to use DB and want to control version too!".

## Usage

```
pygration create --name=table_name
```

`create` generate migration file to create table.

```
pygration alter --name=table_name
```

`alter` generate migration file to alter table.

```
pygration upgrade
```

`upgrade` upgrade database schema.

```
pygration downgrade [OPTIONS]
Options:
  -v, --version INTEGER Roll back to the specified version
```

`downgrade` downgrade database schema.  
If the `-v` option is not specified, roll back step to step.