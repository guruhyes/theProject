/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package templatesbuilder;

import java.awt.*;
import javax.swing.*;

public class FooSwing2 {
   public static void main(String[] args) {
      JTextArea chatArea = new JTextArea(8, 40);
      chatArea.setEditable(false);
      chatArea.setFocusable(false);
      JScrollPane chatScroll = new JScrollPane(chatArea);
      JPanel chatPanel = new JPanel(new BorderLayout());
      chatPanel.add(new JLabel("Chat:", SwingConstants.LEFT), BorderLayout.PAGE_START);
      chatPanel.add(chatScroll);

      JTextField inputField = new JTextField(40);
      JButton sendBtn = new JButton("Send");
      JPanel inputPanel = new JPanel();
      inputPanel.setLayout(new BoxLayout(inputPanel, BoxLayout.LINE_AXIS));
      inputPanel.add(inputField);
      inputPanel.add(sendBtn);

      JPanel youLabelPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
      youLabelPanel.add(new JLabel("You:"));

      JPanel mainPanel = new JPanel();
      mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.PAGE_AXIS));
      mainPanel.add(chatPanel);
      mainPanel.add(Box.createVerticalStrut(10));
      mainPanel.add(youLabelPanel);
      mainPanel.add(inputPanel);

      JFrame frame = new JFrame("Foo");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.add(mainPanel);
      frame.pack();
      frame.setLocationRelativeTo(null);
      frame.setVisible(true);
   }
}
