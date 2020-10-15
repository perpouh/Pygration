# -*- coding: utf-8 -*-
# %%
import click
import datetime
import shutil
import sys
import os

@click.command()
@click.argument('function', default="help")
@click.option('--name', default="")
def main(function, name):
  """
  FUNCTION:\n
    create: create database schema.\n
    upgrade: upgrade database schema.\n
    downgrade: downgrade database schema.
  """
  if function == "init":
    click.echo("init")
  elif function == "help":
    click.echo(__doc__) # TODO: 出ない、なぜ
  elif function == "create":
    create(name)
  elif function == "upgrade":
    upgrade()
  else:
    click.echo("Hello")

def create(name):
  if name == "":
    click.echo("--nameを指定してください")
    sys.exit()

  # フォルダが存在するか確認
  path = os.getcwd() + '/db/migrate'
  click.echo(path)
  if(os.path.exists(path) == False):
    # フォルダを作成していいか確認
    if(click.confirm("Are you sure?")):
      click.echo("Creating directories...")
      os.makedirs(path)
    else:
      click.echo("処理を中断しました")
      sys.exit()


  # ファイル作成
  # templateからcreate.pyをコピーしてタイムスタンプとテーブル名埋め込んで書式はどーすっかなー
  ymdhms = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
  filename = ymdhms + '_create_' + name + '.py'
  shutil.copy(os.path.dirname(__file__) + '/template/create.py', os.getcwd() + '/db/migrate/' + filename)
  click.echo(path)

def upgrade():
  # フォルダが存在するか確認
  # 未処理ファイルが存在するか確認
  # スキーマファイル更新
  # DB更新
  click.echo("upgraded")