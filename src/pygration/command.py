# -*- coding: utf-8 -*-
# %%
import sys
import click

@click.command()
@click.argument('function', default="help")
@click.option('--force/', '-f/', default=False)
@click.option('--name')
def main(function, force, name):
  """
  FUNCTION:\n
    create: create database schema.\n
    upgrade: upgrade database schema.\n
    downgrade: downgrade database schema.
  """
  if function == "help":
    click.echo(__doc__) # TODO: 出ない、なぜ
  elif function == "create":
    create(force)
  elif function == "upgrade":
    upgrade()
  else:
    click.echo("Hello")

def create(force):
  # フォルダが存在するか確認
  # 無ければ作成
  # ファイル作成
  click.echo("created")

def upgrade():
  # フォルダが存在するか確認
  # 未処理ファイルが存在するか確認
  # スキーマファイル更新
  # DB更新
  click.echo("upgraded")