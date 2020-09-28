/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package templatesbuilder;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import static java.nio.file.StandardCopyOption.REPLACE_EXISTING;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Stream;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import org.apache.commons.io.FileUtils;

/**
 *
 * @author guruhyes
 */
public class Builder extends javax.swing.JFrame {

    /**
     * Creates new form Builder
     */
    JButton bt = new JButton("bt");
    JTextField[] _name = new JTextField[1];
    JTextField[] _icon = new JTextField[1];
    JTextField[] _width = new JTextField[1];
    JTextField[] _height = new JTextField[1];
    JTextField[] _left = new JTextField[1];
    JTextField[] _top = new JTextField[1];
    JTextField[] _href = new JTextField[1];
    
    JTextField[] _nameM = new JTextField[1];
    JTextField[] _iconM = new JTextField[1];
    JTextField[] _widthM = new JTextField[1];
    JTextField[] _heightM = new JTextField[1];
    JTextField[] _text = new JTextField[1];
    JTextField[] _hrefM = new JTextField[1];
    int i=0;
    int x=0;
    public Builder() {
        initComponents();
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        bt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btActionPerformed(evt);
            }
        });
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        txtFolderGenerate = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        txtDesktopMenu = new javax.swing.JTextField();
        btnGenerateDesktopMenu = new javax.swing.JButton();
        txtGenerateMenu = new javax.swing.JTextField();
        jButton2 = new javax.swing.JButton();
        jPanel2 = new javax.swing.JPanel();
        jPanel3 = new javax.swing.JPanel();
        jButton3 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jButton1.setText("browse");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        btnGenerateDesktopMenu.setText("generate Desktop");
        btnGenerateDesktopMenu.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGenerateDesktopMenuActionPerformed(evt);
            }
        });

        jButton2.setText("generate Menu");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(193, 193, 193)
                .addComponent(txtGenerateMenu, javax.swing.GroupLayout.PREFERRED_SIZE, 48, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(26, 26, 26)
                .addComponent(jButton2)
                .addContainerGap(363, Short.MAX_VALUE))
            .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(jPanel1Layout.createSequentialGroup()
                    .addGap(194, 194, 194)
                    .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(jPanel1Layout.createSequentialGroup()
                            .addComponent(txtDesktopMenu, javax.swing.GroupLayout.PREFERRED_SIZE, 50, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(18, 18, 18)
                            .addComponent(btnGenerateDesktopMenu))
                        .addGroup(jPanel1Layout.createSequentialGroup()
                            .addComponent(txtFolderGenerate, javax.swing.GroupLayout.PREFERRED_SIZE, 262, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(27, 27, 27)
                            .addComponent(jButton1)))
                    .addContainerGap(195, Short.MAX_VALUE)))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap(97, Short.MAX_VALUE)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtGenerateMenu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton2))
                .addGap(43, 43, 43))
            .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(jPanel1Layout.createSequentialGroup()
                    .addGap(17, 17, 17)
                    .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(txtFolderGenerate, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(jButton1))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                    .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(txtDesktopMenu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(btnGenerateDesktopMenu))
                    .addContainerGap(84, Short.MAX_VALUE)))
        );

        jPanel2.setBackground(new java.awt.Color(0, 153, 153));

        jPanel3.setBackground(new java.awt.Color(0, 153, 153));

        jButton3.setText("Generate");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addComponent(jPanel1, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addComponent(jPanel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addGroup(layout.createSequentialGroup()
                .addGap(259, 259, 259)
                .addComponent(jButton3)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, 247, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 34, Short.MAX_VALUE)
                .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, 218, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(28, 28, 28)
                .addComponent(jButton3)
                .addGap(21, 21, 21))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
        JFileChooser chooser = new JFileChooser();
        chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        chooser.showOpenDialog(null);
        
        txtFolderGenerate.setText(chooser.getSelectedFile().toString());
    }//GEN-LAST:event_jButton1ActionPerformed
    private void copyFolder(File sourceFolder, File destinationFolder) throws IOException
    {
        //Check if sourceFolder is a directory or file
        //If sourceFolder is file; then copy the file directly to new location
        if (sourceFolder.isDirectory()) 
        {
            //Verify if destinationFolder is already present; If not then create it
            if (!destinationFolder.exists()) 
            {
                destinationFolder.mkdir();
                System.out.println("Directory created :: " + destinationFolder);
            }
             
            //Get all files from source directory
            String files[] = sourceFolder.list();
             
            //Iterate over all files and copy them to destinationFolder one by one
            for (String file : files) 
            {
                File srcFile = new File(sourceFolder, file);
                File destFile = new File(destinationFolder, file);
                 
                //Recursive function call
                copyFolder(srcFile, destFile);
            }
        }
        else
        {
            //Copy the file content from one place to another 
            Files.copy(sourceFolder.toPath(), destinationFolder.toPath(), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("File copied :: " + destinationFolder);
        }
    }

    private void cop(){
        File sourceFolder = new File(System.getProperty("user.dir")+"/template/base/");
         
        //Target directory where files should be copied
        File destinationFolder = new File(System.getProperty("user.dir")+"/generateFolder/");
 
        try {
            //Call Copy function
            copyFolder(sourceFolder ,destinationFolder);
            JOptionPane.showMessageDialog(null, "done");
        } catch (IOException ex) {
            Logger.getLogger(Builder.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
//    public  void copyFolder(Path src, Path dest) throws IOException {
//        try (Stream<Path> stream = Files.walk(src)) {
//            stream.forEach(source -> copy(source, dest.resolve(src.relativize(source))));
//        }
//    }
// 
//    private void copy(Path source, Path dest) {
//        try {
//            Files.copy(source, dest, REPLACE_EXISTING);
//        } catch (Exception e) {
//            throw new RuntimeException(e.getMessage(), e);
//        }
//    }
    private void btnGenerateDesktopMenuActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGenerateDesktopMenuActionPerformed
        // TODO add your handling code here:
        jPanel2.removeAll();
        _name = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        _icon = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        _width = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        _height = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        _top = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        _left = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        _href = new JTextField[Integer.parseInt(txtDesktopMenu.getText())];
        if(txtDesktopMenu.getText().equals("") || txtDesktopMenu.getText().equals("0")){
            JOptionPane.showMessageDialog(null, "tidak Boleh Kosong atau 0");
        }else{
            for(int i=0;i<Integer.parseInt(txtDesktopMenu.getText());i++){
                JLabel _lblName = new JLabel("name");
                _name[i] = new JTextField();
                _name[i].setPreferredSize(new Dimension(150, 40));
                JLabel _lblIcon = new JLabel("Icon");
                _icon[i] = new JTextField();
                _icon[i].setPreferredSize(new Dimension(150, 40));
                JLabel _lblWidth = new JLabel("Width");
                _width[i] = new JTextField("400");
                _width[i].setPreferredSize(new Dimension(150, 40));
                JLabel _lblheight = new JLabel("Width");
                _height[i] = new JTextField("400");
                _height[i].setPreferredSize(new Dimension(150, 40));
                JLabel _lblTop = new JLabel("Top");
                _top[i] = new JTextField("100");
                _top[i].setPreferredSize(new Dimension(150, 40));
                JLabel _lblLeft = new JLabel("Left");
                _left[i] = new JTextField("200");
                _left[i].setPreferredSize(new Dimension(150, 40));
                JLabel _lblHref =  new JLabel("Href");
                _href[i] = new JTextField("#");
                _href[i].setPreferredSize(new Dimension(150, 40));
                JPanel jpan = new JPanel();
                jpan.setLayout(new FlowLayout());
                jpan.setPreferredSize(new Dimension(jPanel2.getWidth(),50));
                jPanel2.add(jpan);
                jpan.add(_lblName);
                jpan.add(_name[i]);
                jpan.add(_lblIcon);
                jpan.add(_icon[i]);
                jpan.add(_lblWidth);
                jpan.add(_width[i]);
                jpan.add(_lblheight);
                jpan.add(_height[i]);
                jpan.add(_lblTop);
                jpan.add(_top[i]);
                jpan.add(_lblLeft);
                jpan.add(_left[i]);
                jpan.add(_lblHref);
                jpan.add(_href[i]);
                jPanel2.revalidate();
                jPanel2.repaint();
                
            }
            
        }
        
        
        

    }//GEN-LAST:event_btnGenerateDesktopMenuActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        // TODO add your handling code here:
        jPanel3.removeAll();
        _nameM = new JTextField[Integer.parseInt(txtGenerateMenu.getText())];
        _iconM = new JTextField[Integer.parseInt(txtGenerateMenu.getText())];
        _widthM = new JTextField[Integer.parseInt(txtGenerateMenu.getText())];
        _heightM = new JTextField[Integer.parseInt(txtGenerateMenu.getText())];
        _text = new JTextField[Integer.parseInt(txtGenerateMenu.getText())];
        _hrefM = new JTextField[Integer.parseInt(txtGenerateMenu.getText())];
        if(txtGenerateMenu.getText().equals("") || txtGenerateMenu.getText().equals("0")){
            JOptionPane.showMessageDialog(null, "tidak Boleh Kosong atau 0");
        }else{
            for(int x=0;x<Integer.parseInt(txtGenerateMenu.getText());x++){
                JLabel _lblNameM = new JLabel("Name");
                _nameM[x] = new JTextField();
                _nameM[x].setPreferredSize(new Dimension(150, 40));
                JLabel _lblIconM = new JLabel("Icon");
                _iconM[x] = new JTextField();
                _iconM[x].setPreferredSize(new Dimension(150, 40));
                JLabel _lblWidthM = new JLabel("Width");
                _widthM[x] = new JTextField("400");
                _widthM[x].setPreferredSize(new Dimension(150, 40));
                JLabel _lblHeightM = new JLabel("Height");
                _heightM[x] = new JTextField("200");
                _heightM[x].setPreferredSize(new Dimension(150, 40));
                JLabel _lblText = new JLabel("Text");
                _text[x] = new JTextField();
                _text[x].setPreferredSize(new Dimension(150, 40));
                JLabel _lblHrefM = new JLabel("Href");
                _hrefM[x] = new JTextField("#");
                _hrefM[x].setPreferredSize(new Dimension(150, 40));
                JPanel jpan = new JPanel();
                jpan.setLayout(new FlowLayout());
                jpan.setPreferredSize(new Dimension(jPanel3.getWidth(),50));
                jPanel3.add(jpan);
                jpan.add(_lblNameM);
                jpan.add(_nameM[x]);
                jpan.add(_lblIconM);
                jpan.add(_iconM[x]);
                jpan.add(_lblWidthM);
                jpan.add(_widthM[x]);
                jpan.add(_lblHeightM);
                jpan.add(_heightM[x]);
                jpan.add(_lblText);
                jpan.add(_text[x]);
                jpan.add(_lblHrefM);
                jpan.add(_hrefM[x]);
                jPanel3.revalidate();
                jPanel3.repaint();
                
            }
            
        }
        
    }//GEN-LAST:event_jButton2ActionPerformed

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        // TODO add your handling code here:

        String _teol = "";
        String _menul = "";
        for(int j=0;j<Integer.parseInt(txtDesktopMenu.getText());j++){
            _teol = _teol+"{name:'"+_name[j].getText()+"',icon:'"+_icon[j].getText()+"',width:'"+_width[j].getText()+"',height:'"+_height[j].getText()+"',left:'"+_left[j].getText()+"',top:'"+_top[j].getText()+"',href:'"+_href[j].getText()+"'},\n";
        }
        for(int k=0;k<Integer.parseInt(txtGenerateMenu.getText());k++){
            _menul = _menul +"{text:'"+_text[k].getText()+"',"
                    + "handler:function(){"
                    + "$('body').desktop('openApp',{"
                    + "icon:'"+_iconM[k].getText()+"',name:'"+_nameM[k].getText()+"',width:'"+_widthM[k].getText()+"',height:'"+_heightM[k].getText()+"',href:'"+_hrefM[k].getText()+"'"
                    + "})"
                    + "}"
                    + "},\n";
        }
        String app = "apps:[\n"
                + _teol+"\n],menus:[\n"+_menul+"\n],";
        System.out.println(app);
        try{
           File htmlTemplateFile = new File("template/desktop.html");
            String htmlString = FileUtils.readFileToString(htmlTemplateFile);
            //String title = "New Page";
            //String body = "This is Body \n waow sekali \n ya kan";
            //htmlString = htmlString.replace("$title", title);
            htmlString = htmlString.replace("$App", app);
            File newHtmlFile = new File("generateFolder/generate.html");
            FileUtils.writeStringToFile(newHtmlFile, htmlString); 
            cop();
        }catch(Exception e){
            System.out.println(e);
        }
        
    }//GEN-LAST:event_jButton3ActionPerformed
    private void btActionPerformed(java.awt.event.ActionEvent evt){
        for(int y=0;y<Integer.parseInt(txtDesktopMenu.getText());y++){
            System.out.println(_name[y].getText());
        }
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Builder.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Builder.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Builder.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Builder.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Builder().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnGenerateDesktopMenu;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JTextField txtDesktopMenu;
    private javax.swing.JTextField txtFolderGenerate;
    private javax.swing.JTextField txtGenerateMenu;
    // End of variables declaration//GEN-END:variables
}
