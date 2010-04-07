#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk, gtk.glade
from Config import *
from ReplaceCore import *
import ReplaceCore


'''
Created on 2010-4-7

@author: pjq
'''
#RCW:Replace Chinese Word

class RCW:
    """
    The main class for RCW.
    """
    
    def __init__(self):
        """
        Init do something init here.
        """
        
        mainTree = gtk.glade.XML(main_view_glade)
        
        event_dict = {'on_replace_button_clicked':self.on_replace_button_clicked,
                      'on_recovery_button_clicked':self.on_recovery_button_clicked,
                       'on_done_button_clicked':self.on_done_button_clicked}
        mainTree.signal_autoconnect(event_dict)
        
        
        self.input_label = mainTree.get_widget('input_label')
        self.input_entry = mainTree.get_widget('input_entry')
        self.replace_button = mainTree.get_widget('replace_button')
        self.recovery_button = mainTree.get_widget('recovery_button')        
        self.replaced_textview = mainTree.get_widget('replaced_textview')
        
        self.replace_core = StrReplace()
          
        self.replaced_textview_buffer = self.replaced_textview.get_buffer()
  
    def on_replace_button_clicked(self, widget, data=None):
        """
        When the replace button clicked,run here.
        """
        text = self.input_entry.get_text()
        text = self.replace_core.replaceStr(text)
        
        self.replaced_textview_buffer.set_text(text)
       
    def on_recovery_button_clicked(self, widget, data=None):
        """
         When the recovery button clicked,run here.
        """
            
        # get_text方法的前两个参数指定取buffer的起始和终止位置,类型是gtk.TextIter
         # 要获得诸如从头到当前光标间的内容之类的东西,可以查看下gtk.TextBuffer的get_*_iter()方法  
        start = self.replaced_textview_buffer.get_start_iter()
        end = self.replaced_textview_buffer.get_end_iter()
            
        text = self.replaced_textview_buffer.get_text(start, end)
        text = self.replace_core.recoveryStr(text)
        
        self.replaced_textview_buffer.set_text(text)
       
        
    def on_done_button_clicked(self, widget, data=None):
        """
         When the done button clicked,run here.
        """
        gtk.main_quit()




def main():
    gtk.main()


if __name__ == '__main__':
    print 'main'    
    RCW()
    main()
