# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 09:27:48 2023

@author: khairulakmal
"""
import click
from sijilify import sijilify
 
sijil = sijilify()

def read_template(template):
    """Read identify template configuration."""
    click.clear()
    number = 0
    if template == None: 
        click.echo('List of templates')
        for key in sijil.list_template():
            number = number +1 
            click.echo(f'{number} : {key}')
    else:
        click.echo(f'Template configuration for {template}\n')
        read = sijil.read_template(template)
        for keys, value in read.items():
            number = number + 1
            print(f'{number}.{keys} : {value}')    

@click.group()
def cli():
    """This script showcases different terminal UI helpers in Click."""
    pass

@cli.command() 
@click.option("-t","--template", default=None, help="Template to preview",)
@click.option("-n","--number", default=-1, type=int, help="The number of data to preview",)
def preview(template, number):
    """Preview the template prior for export."""
    click.clear()
    if template == None:
        sijil.load_config()
    else:
        sijil.load_config(template)
        
    sijil.preview(number)


@cli.command()
@click.option("-t","--template", default=None, help="Template to export",)
def export(template):
    """Export the template to specify template folder."""
    click.clear()
    if template == None:
        sijil.load_config()
    else:
        sijil.load_config(template)
        
    sijil.generated()

@cli.command()
@click.argument('template')
def create(template):
    """Create new template and folder."""
    sijil.register(template)

@cli.command()
@click.option("-t","--template", default=None, help="Template configuration.",)
def read(template):
    read_template(template)

@cli.command()
@click.option("-t", "--template", help="The template name for the update.",)
@click.option("-f", "--font", default=None, help="Font.",)
@click.option("-s", "--size", default=None, help="Size of the font.",)
@click.option("-c", "--color", default=None, help="Color of the font.",)
@click.option("-y", "--y", default=None, help="Determine the y position of the name appear on the template.",)
@click.option("-n", "--name", default=None, help="Name file for list name to be printed on template in .txt format.",)
@click.option("-i", "--image", default=None, help="Name file for template in .jpg format.",)
def update(template, font, size, color, y, name, image):
    """Update identify template configuration."""
    if font:
        sijil.update(section=template, font=font)
    if size:
        sijil.update(section=template, font_size=size)
    if color:
        sijil.update(section=template, font_color=color)
    if y:
        sijil.update(section=template, y_position=y)
    if name:
        sijil.update(section=template, file_list=name)
    if image:
        sijil.update(section=template, file_certificate=image)
    # read_template(template)

@cli.command()
def delete():
    """Delete identify template configuration."""
    pass  

@cli.command()
def clear():
    """Clear the screen"""
    click.clear()
        
  
if __name__ == '__main__':
    cli()

    
    