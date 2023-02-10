/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JeuDeLaVie;
import java.awt.Dimension;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.GridLayout;
import java.awt.Color;
/**
 *
 * @author bperr
 */
public class Plateau extends JFrame{
    
    private boolean[][] grille;
    private JPanel p,zoneD,zoneC;
    private JPanel[][] Igrille;
    private JButton oneGen,restart,nGen;
    private JLabel gen;
    private int numGen;
    
    public Plateau(int tx,int ty)
    {
        numGen=0;
        
        // Fenêtre
        p = new JPanel();
        JScrollPane scroll= new JScrollPane(p);
        add(scroll);
        p.setLayout(new BoxLayout(p,1));
        JLabel titre = new JLabel("Bienvenue dans le jeu de la vie !");
        titre.setAlignmentX(CENTER_ALIGNMENT);
        p.add(titre);
        
        zoneD = new JPanel();
        zoneD.setLayout(new GridLayout(tx,ty));
        zoneD.setAlignmentX(CENTER_ALIGNMENT);
        zoneD.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));//top,left,bottom,right;
        //zoneD.setPreferredSize(new Dimension(20*tx,20*ty));
        p.add(zoneD);
        
        gen = new JLabel("Génération numéro : "+numGen);
        gen.setAlignmentX(CENTER_ALIGNMENT);
        p.add(gen);
        
        zoneC = new JPanel();
        zoneC.setLayout(new BoxLayout(zoneC,0));
        oneGen = new JButton("Faire une génération");
        oneGen.addActionListener(new NextGenListener(this)); 
        zoneC.add(oneGen);
        nGen = new JButton("Faire des générations");
        nGen.addActionListener(new NGenListener(this));
        zoneC.add(nGen);
        restart = new JButton("Rénitialiser");
        restart.addActionListener(new ResetListener(this));
        zoneC.add(restart);
        p.add(zoneC);
        
        grille = new boolean[tx][ty];
        Igrille=new JPanel[tx][ty];
        
        for (int i=0;i<tx;i++) { // i: numero de ligne
            for (int j=0;j<ty;j++) { // j: numero de colonne
                if (Math.random()>0.5)
                {
                    grille[i][j] = true;
                    Igrille[i][j] = new JPanel();
                    Igrille[i][j].setBackground(Color.black);
                    Igrille[i][j].setPreferredSize(new Dimension(750/tx,750/ty));
                    zoneD.add(Igrille[i][j]);
                }
                else
                {
                    grille[i][j]=false;
                    Igrille[i][j] = new JPanel();
                    Igrille[i][j].setBackground(Color.white);
                    Igrille[i][j].setPreferredSize(new Dimension(750/tx,750/ty));
                    zoneD.add(Igrille[i][j]);
                }
            }
        }
        
        
        
        
        //setSize(800,830);
        pack();
        setLocationRelativeTo(null);
        setTitle("Le jeu de la vie");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    @Override
    public String toString() {
        String chn1="";
        for (int i=0; i<grille.length;i++) {
            for (int j=0; j<grille[0].length;j++) {
                
                if (grille[i][j])
                {
                    chn1+="X";
                }
                else
                {
                    chn1+="O";
                }
                chn1+="  ";
            }
            chn1+="\n";
        }
        return chn1;
    }
    
    public void reset()
    {
        numGen=0;
        gen.setText("Génération numéro : "+numGen);
        for (int i=0;i<grille.length;i++) {
            for (int j=0;j<grille[0].length;j++) {
                if (Math.random()>0.5)
                {
                    grille[i][j] = true;
                    Igrille[i][j].setBackground(Color.black);
                    Igrille[i][j].repaint();
                }
                else
                {
                    grille[i][j]=false;
                    Igrille[i][j].setBackground(Color.white);
                    Igrille[i][j].repaint();
                }
            }
        }
    }
    
    public void nextStep()
    {
        numGen++;
        gen.setText("Génération numéro : "+numGen);
        int tx=grille.length;
        int ty= grille[0].length;
        
        // copie
        boolean[][] g = new boolean[tx][ty];
        for (int i=0; i<tx;i++) {
            for (int j=0; j<ty;j++) {
                g[i][j]=grille[i][j];
            }
        }
        
        // Première colonne
            // Angle sup gauche
        int nbVoisins=0;
        if (g[0][1]) { nbVoisins++; } // A droite
        if (g[1][1]) { nbVoisins++; } // En bas a droite
        if (g[1][0]) { nbVoisins++; } // En bas
        if ((g[0][0])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
        {
            grille[0][0]=false;
            Igrille[0][0].setBackground(Color.white);
            Igrille[0][0].repaint();
        }
        if ((!g[0][0])&&(nbVoisins==3)) // Morte mais va vivre
        {
            grille[0][0]=true;
            Igrille[0][0].setBackground(Color.black);
            Igrille[0][0].repaint();
        }
            //Angle inf gauche
        nbVoisins=0;
        if (g[tx-2][0]) { nbVoisins++; } // En haut
        if (g[tx-2][1]) { nbVoisins++; } // En haut à droite
        if (g[tx-1][1]) { nbVoisins++; } // A droite
        if ((g[tx-1][0])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
        {
            grille[tx-1][0]=false;
            Igrille[tx-1][0].setBackground(Color.white);
            Igrille[tx-1][0].repaint();
        }
        if ((!g[tx-1][0])&&(nbVoisins==3)) // Morte mais va vivre
        {
            grille[tx-1][0]=true;
            Igrille[tx-1][0].setBackground(Color.black);
            Igrille[tx-1][0].repaint();
        }
            // Le reste
        for (int i=1;i<tx-1;i++)
        {
            int nbV=0;
            if (g[i-1][0]) { nbV++; } // En haut
            if (g[i-1][1]) { nbV++; } // En haut à droite
            if (g[i][1]) { nbV++; } // A droite
            if (g[i+1][1]) { nbV++; } // En bas à droite
            if (g[i+1][0]) { nbV++; } // En bas
            
            if ((g[i][0])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
            {
                grille[i][0]=false;
                Igrille[i][0].setBackground(Color.white);
                Igrille[i][0].repaint();
            }
            if ((!g[i][0])&&(nbV==3)) // Morte mais va vivre
            {
                grille[i][0]=true;
                Igrille[i][0].setBackground(Color.black);
                Igrille[i][0].repaint();
            }
        }
        
        
        // Derniere colonne
            // Angle sup droit
        nbVoisins=0;
        if (g[1][ty-1]) { nbVoisins++; } // En bas
        if (g[1][ty-2]) { nbVoisins++; } // En bas a gauche
        if (g[0][ty-2]) { nbVoisins++; } // A gauche
        if ((g[0][ty-1])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
        {
            grille[0][ty-1]=false;
            Igrille[0][ty-1].setBackground(Color.white);
            Igrille[0][ty-1].repaint();
        }
        if ((!g[0][ty-1])&&(nbVoisins==3)) // Morte mais va vivre
        {
            grille[0][ty-1]=true;
            Igrille[0][ty-1].setBackground(Color.black);
            Igrille[0][ty-1].repaint();
        }
            // Angle inf droit
        nbVoisins=0;
        if (g[tx-1][ty-2]) { nbVoisins++; } // A gauche
        if (g[tx-2][ty-2]) { nbVoisins++; } // En haut a gauche
        if (g[tx-2][ty-1]) { nbVoisins++; } // En haut
        if ((g[tx-1][ty-1])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
        {
            grille[tx-1][ty-1]=false;
            Igrille[tx-1][ty-1].setBackground(Color.white);
            Igrille[tx-1][ty-1].repaint();
        }
        if ((!g[tx-1][ty-1])&&(nbVoisins==3)) // Morte mais va vivre
        {
            grille[tx-1][ty-1]=true;
            Igrille[tx-1][ty-1].setBackground(Color.black);
            Igrille[tx-1][ty-1].repaint();
        }
            // Le reste
        for (int i=1;i<tx-1;i++)
        {
            int nbV=0;
            if (g[i+1][ty-1]) { nbV++; } // En bas
            if (g[i+1][ty-2]) { nbV++; } // En bas à gauche
            if (g[i][ty-2]) { nbV++; } // A gauche
            if (g[i-1][ty-2]) { nbV++; } // En haut à gauche
            if (g[i-1][ty-1]) { nbV++; } // En haut
            
            if ((g[i][ty-1])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
            {
                grille[i][ty-1]=false;
                Igrille[i][ty-1].setBackground(Color.white);
                Igrille[i][ty-1].repaint();
            }
            if ((!g[i][ty-1])&&(nbV==3)) // Morte mais va vivre
            {
                grille[i][ty-1]=true;
                Igrille[i][ty-1].setBackground(Color.black);
                Igrille[i][ty-1].repaint();
            }
        }
        
        // Première ligne
        for (int j=1;j<ty-1;j++)
        {
            int nbV=0;
            if (g[0][j+1]) { nbV++; } // A droite
            if (g[1][j+1]) { nbV++; } // En bas à droite
            if (g[1][j]) { nbV++; } // En bas
            if (g[1][j-1]) { nbV++; } // En bas à gauche
            if (g[0][j-1]) { nbV++; } // A gauche
            
            if ((g[0][j])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
            {
                grille[0][j]=false;
                Igrille[0][j].setBackground(Color.white);
                Igrille[0][j].repaint();
            }
            if ((!g[0][j])&&(nbV==3)) // Morte mais va vivre
            {
                grille[0][j]=true;
                Igrille[0][j].setBackground(Color.black);
                Igrille[0][j].repaint();
            }
        }
        
        // Derniere ligne
        for (int j=1;j<ty-1;j++)
        {
            int nbV=0;
            if (g[tx-1][j-1]) { nbV++; } // A gauche
            if (g[tx-2][j-1]) { nbV++; } // En haut a gauche
            if (g[tx-2][j]) { nbV++; } // En haut
            if (g[tx-2][j+1]) { nbV++; } // En haut à droite
            if (g[tx-1][j+1]) { nbV++; } // A droite
            
            if ((g[tx-1][j])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
            {
                grille[tx-1][j]=false;
                Igrille[tx-1][j].setBackground(Color.white);
                Igrille[tx-1][j].repaint();
            }
            if ((!g[tx-1][j])&&(nbV==3)) // Morte mais va vivre
            {
                grille[tx-1][j]=true;
                Igrille[tx-1][j].setBackground(Color.black);
                Igrille[tx-1][j].repaint();
            }
        }
        
        // Grille centrale
        for (int i=1;i<tx-1;i++) {
            for (int j=1;j<ty-1;j++) {
                
                int nbV=0;
                if (g[i-1][j]) { nbV++; } // En haut
                if (g[i-1][j+1]) { nbV++; } // En haut a droite
                if (g[i][j+1]) { nbV++; } // A droite
                if (g[i+1][j+1]) { nbV++; } // En bas a droite
                if (g[i+1][j]) { nbV++; } // En bas
                if (g[i+1][j-1]) { nbV++; } // En bas a gauche
                if (g[i][j-1]) { nbV++; } // A gauche
                if (g[i-1][j-1]) { nbV++; } // En haut a gauche
                
                if ((g[i][j])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
                {
                    grille[i][j]=false;
                    Igrille[i][j].setBackground(Color.white);
                    Igrille[i][j].repaint();
                }
                if ((!g[i][j])&&(nbV==3)) // Morte mais va vivre
                {
                    grille[i][j]=true;
                    Igrille[i][j].setBackground(Color.black);
                    Igrille[i][j].repaint();
                }
            }
                
        }
        
    }
    
    public void faireNStep(int n)
    {
        for (int i=0;i<n;i++) 
        {
            nextStep();
        }
    }
    
    public void nextStep(int xmin, int xmax, int ymin, int ymax)
    {
        numGen++;
        gen.setText("Génération numéro : "+numGen);
        int tx=grille.length;
        int ty= grille[0].length;
        
        // copie partielle
        int xcmin,xcmax,ycmin,ycmax; // Indice de copie
        if (xmin==0) { xcmin=0;} else {xcmin=xmin-1;}
        if (xmax==tx) { xcmax=tx;} else {xcmax=xmax+1;}
        if (ymin==0) { ycmin=0;} else {ycmin=ymin-1;}
        if (ymax==ty) { ycmax=ty;} else {ycmax=ymax+1;}
        
        System.out.println(xcmin+","+xcmax+","+ycmin+","+ycmax);
        boolean[][] g = new boolean[xcmax-xcmin][ycmax-ycmin];
        synchronized(this) { // La copie doit se faire avant la modification
            for (int i=xcmin; i<xcmax;i++) {
                for (int j=ycmin; j<ycmax;j++) {
                    g[i-xcmin][j-ycmin]=grille[i][j];
                }
            }
        }
        System.out.println("Copie faite");
        int xmin2,xmax2,ymin2,ymax2;
        
        if (ymin==0) // ycmin=0, on ne l'écrit pas
        {
            ymin2=1;
        // Première colonne
        int XMIN, XMAX;
            if (xmin==0) // xcmin=0, on ne l'écrit pas
            {
                // Angle sup gauche
                int nbVoisins=0;
                if (g[0][1]) { nbVoisins++; } // A droite
                if (g[1][1]) { nbVoisins++; } // En bas a droite
                if (g[1][0]) { nbVoisins++; } // En bas
                if ((g[0][0])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
                {
                    grille[0][0]=false;
                    Igrille[0][0].setBackground(Color.white);
                    Igrille[0][0].repaint();
                }
                if ((!g[0][0])&&(nbVoisins==3)) // Morte mais va vivre
                {
                    grille[0][0]=true;
                    Igrille[0][0].setBackground(Color.black);
                    Igrille[0][0].repaint();
                }
                XMIN=1;
            }
            else 
            {
                XMIN=xmin;            
            }
            
            if (xmax==tx) {
                //Angle inf gauche
                int nbVoisins=0;
                if (g[tx-2-xcmin][0]) { nbVoisins++; } // En haut
                if (g[tx-2-xcmin][1]) { nbVoisins++; } // En haut à droite
                if (g[tx-1-xcmin][1]) { nbVoisins++; } // A droite
                if ((g[tx-1-xcmin][0])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
                {
                    grille[tx-1][0]=false;
                    Igrille[tx-1][0].setBackground(Color.white);
                    Igrille[tx-1][0].repaint();
                }
                if ((!g[tx-1-xcmin][0])&&(nbVoisins==3)) // Morte mais va vivre
                {
                    grille[tx-1][0]=true;
                    Igrille[tx-1][0].setBackground(Color.black);
                    Igrille[tx-1][0].repaint();
                }
                XMAX=tx-1;
            }
            else
            {
                XMAX=xmax;
            }
            
                // Le reste
            for (int i=XMIN;i<XMAX;i++)
            {
                int nbV=0;
                if (g[i-1-xcmin][0]) { nbV++; } // En haut
                if (g[i-1-xcmin][1]) { nbV++; } // En haut à droite
                if (g[i-xcmin][1]) { nbV++; } // A droite
                if (g[i+1-xcmin][1]) { nbV++; } // En bas à droite
                if (g[i+1-xcmin][0]) { nbV++; } // En bas

                if ((g[i-xcmin][0])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
                {
                    grille[i][0]=false;
                    Igrille[i][0].setBackground(Color.white);
                    Igrille[i][0].repaint();
                }
                if ((!g[i-xcmin][0])&&(nbV==3)) // Morte mais va vivre
                {
                    grille[i][0]=true;
                    Igrille[i][0].setBackground(Color.black);
                    Igrille[i][0].repaint();
                }
            }
        
        }
        else
        {
            ymin2=ymin;
        }
        
        if (ymax==ty)
        {
            ymax2=ty-1;
        // Derniere colonne
            int XMIN,XMAX;
            if(xmin==0) // xcmin=0, on ne l'écrit pas
            {
                // Angle sup droit
                int nbVoisins=0;
                if (g[1][ty-1-ycmin]) { nbVoisins++; } // En bas
                if (g[1][ty-2-ycmin]) { nbVoisins++; } // En bas a gauche
                if (g[0][ty-2-ycmin]) { nbVoisins++; } // A gauche
                if ((g[0][ty-1-ycmin])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
                {
                    grille[0][ty-1]=false;
                    Igrille[0][ty-1].setBackground(Color.white);
                    Igrille[0][ty-1].repaint();
                }
                if ((!g[0][ty-1-ycmin])&&(nbVoisins==3)) // Morte mais va vivre
                {
                    grille[0][ty-1]=true;
                    Igrille[0][ty-1].setBackground(Color.black);
                    Igrille[0][ty-1].repaint();
                }
                XMIN=1;
            }
            else
            {
                XMIN=xmin;
            }
            
            if (xmax==tx)
            {
                // Angle inf droit
                int nbVoisins=0;
                if (g[tx-1-xcmin][ty-2-ycmin]) { nbVoisins++; } // A gauche
                if (g[tx-2-xcmin][ty-2-ycmin]) { nbVoisins++; } // En haut a gauche
                if (g[tx-2-xcmin][ty-1-ycmin]) { nbVoisins++; } // En haut
                if ((g[tx-1-xcmin][ty-1-ycmin])&&((nbVoisins<2)||(nbVoisins>3))) // Vivante mais va mourir
                {
                    grille[tx-1][ty-1]=false;
                    Igrille[tx-1][ty-1].setBackground(Color.white);
                    Igrille[tx-1][ty-1].repaint();
                }
                if ((!g[tx-1-xcmin][ty-1-ycmin])&&(nbVoisins==3)) // Morte mais va vivre
                {
                    grille[tx-1][ty-1]=true;
                    Igrille[tx-1][ty-1].setBackground(Color.black);
                    Igrille[tx-1][ty-1].repaint();
                }
                XMAX=tx-1;
            }
            else
            {
                XMAX=xmax;
            }
            
                // Le reste
            for (int i=XMIN;i<XMAX;i++)
            {
                int nbV=0;
                if (g[i+1-xcmin][ty-1-ycmin]) { nbV++; } // En bas
                if (g[i+1-xcmin][ty-2-ycmin]) { nbV++; } // En bas à gauche
                if (g[i-xcmin][ty-2-ycmin]) { nbV++; } // A gauche
                if (g[i-1-xcmin][ty-2-ycmin]) { nbV++; } // En haut à gauche
                if (g[i-1-xcmin][ty-1-ycmin]) { nbV++; } // En haut

                if ((g[i-xcmin][ty-1-ycmin])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
                {
                    grille[i][ty-1]=false;
                    Igrille[i][ty-1].setBackground(Color.white);
                    Igrille[i][ty-1].repaint();
                }
                if ((!g[i-xcmin][ty-1-ycmin])&&(nbV==3)) // Morte mais va vivre
                {
                    grille[i][ty-1]=true;
                    Igrille[i][ty-1].setBackground(Color.black);
                    Igrille[i][ty-1].repaint();
                }
            }
        }
        else
        {
            ymax2=ymax;
        }
        
        if (xmin==0) // xcmin=0, on ne l'écrit pas
        {
            xmin2=1;
            // Première ligne
            for (int j=ymin2;j<ymax2;j++)
            {
                int nbV=0;
                if (g[0][j+1-ycmin]) { nbV++; } // A droite
                if (g[1][j+1-ycmin]) { nbV++; } // En bas à droite
                if (g[1][j-ycmin]) { nbV++; } // En bas
                if (g[1][j-1-ycmin]) { nbV++; } // En bas à gauche
                if (g[0][j-1-ycmin]) { nbV++; } // A gauche

                if ((g[0][j-ycmin])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
                {
                    grille[0][j]=false;
                    Igrille[0][j].setBackground(Color.white);
                    Igrille[0][j].repaint();
                }
                if ((!g[0][j-ycmin])&&(nbV==3)) // Morte mais va vivre
                {
                    grille[0][j]=true;
                    Igrille[0][j].setBackground(Color.black);
                    Igrille[0][j].repaint();
                }
            }
        }
        else
        {
            xmin2=xmin;
        }
        
        if (xmax==tx)
        {
            xmax2=tx-1;
            // Derniere ligne
            for (int j=ymin2;j<ymax2;j++)
            {
                int nbV=0;
                if (g[tx-1-xcmin][j-1-ycmin]) { nbV++; } // A gauche
                if (g[tx-2-xcmin][j-1-ycmin]) { nbV++; } // En haut a gauche
                if (g[tx-2-xcmin][j-ycmin]) { nbV++; } // En haut
                if (g[tx-2-xcmin][j+1-ycmin]) { nbV++; } // En haut à droite
                if (g[tx-1-xcmin][j+1-ycmin]) { nbV++; } // A droite

                if ((g[tx-1-xcmin][j-ycmin])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
                {
                    grille[tx-1][j]=false;
                    Igrille[tx-1][j].setBackground(Color.white);
                    Igrille[tx-1][j].repaint();
                }
                if ((!g[tx-1-xcmin][j-ycmin])&&(nbV==3)) // Morte mais va vivre
                {
                    grille[tx-1][j]=true;
                    Igrille[tx-1][j].setBackground(Color.black);
                    Igrille[tx-1][j].repaint();
                }
            }
        }
        else
        {
            xmax2=xmax;
        }
    
        // Grille centrale
        for (int i=xmin2;i<xmax2;i++) {
            for (int j=ymin2;j<ymax2;j++) {
                
                int nbV=0;
                if (g[i-1-xcmin][j-ycmin]) { nbV++; } // En haut
                if (g[i-1-xcmin][j+1-ycmin]) { nbV++; } // En haut a droite
                if (g[i-xcmin][j+1-ycmin]) { nbV++; } // A droite
                if (g[i+1-xcmin][j+1-ycmin]) { nbV++; } // En bas a droite
                if (g[i+1-xcmin][j-ycmin]) { nbV++; } // En bas
                if (g[i+1-xcmin][j-1-ycmin]) { nbV++; } // En bas a gauche
                if (g[i-xcmin][j-1-ycmin]) { nbV++; } // A gauche
                if (g[i-1-xcmin][j-1-ycmin]) { nbV++; } // En haut a gauche
                
                if ((g[i-xcmin][j-ycmin])&&((nbV<2)||(nbV>3))) // Vivante mais va mourir
                {
                    grille[i][j]=false;
                    Igrille[i][j].setBackground(Color.white);
                    Igrille[i][j].repaint();
                }
                if ((!g[i-xcmin][j-ycmin])&&(nbV==3)) // Morte mais va vivre
                {
                    grille[i][j]=true;
                    Igrille[i][j].setBackground(Color.black);
                    Igrille[i][j].repaint();
                }
            }
                
        }
        
    }
    
    public void nextStepWithTreads(int nbThreads)
    {
        int tx = grille.length;
        int ty = grille[0].length;
        Thread[] tabThread = new Thread[nbThreads];
        
        for (int i=0;i<nbThreads;i++)
        {
            tabThread[i] = new Thread(new NextGenThread(i*tx/nbThreads,(i+1)*tx/nbThreads,0,ty,this));
            tabThread[i].start();
        }
        for (int i=0;i<nbThreads;i++)
        {
            try { tabThread[i].join(); } catch (InterruptedException ie) {}
        }
        
    }
    
    public class NextGenThread implements Runnable {
        
        int xmin,xmax,ymin,ymax;
        Plateau source;
        
        @Override
        public void run()
        {
            source.nextStep(xmin,xmax,ymin,ymax);
        }
        
        public NextGenThread(int xm,int xM,int ym,int yM,Plateau p)
        {
            xmin=xm;
            xmax=xM;
            ymin=ym;
            ymax=yM;
            source=p;
        }
    }
    
    public class NextGenListener implements ActionListener{
        
        private Plateau source;
        
        @Override
        public void actionPerformed(ActionEvent e) 
        {
            source.nextStep();
        }
        
        public NextGenListener(Plateau m)
        {
            source=m;
        }
    }
    
    public class NGenListener implements ActionListener{
        
        private Plateau source;
        
        @Override
        public void actionPerformed(ActionEvent e) 
        {
            JFrame ask = new JFrame("Nombre de génération");
            JPanel pan= (JPanel) ask.getContentPane();
            pan.setLayout(new BoxLayout(pan,0));
            SpinnerNumberModel number = new SpinnerNumberModel(10,2,500,1);
            JSpinner spin = new JSpinner(number);
            pan.add(spin);
            JButton val = new JButton("Valider");
            val.addActionListener(new NGenMaker(spin,ask,source));
            val.setPreferredSize(new Dimension(250,60));
            pan.add(val);
            ask.setSize(400,60);
            ask.setLocationRelativeTo(null);
            ask.setVisible(true);
            
        }
        
        public NGenListener(Plateau m)
        {
            source=m;
        }
    }
    
    public class NGenMaker implements ActionListener {
        
        private JSpinner sp;
        private Plateau source;
        private JFrame fenAFermer;
        
        public NGenMaker(JSpinner s, JFrame fen,Plateau fen2)
        {
            sp=s;
            fenAFermer=fen;
            source=fen2;
        }
        public void actionPerformed(ActionEvent e)
        {
            try {
                sp.commitEdit();
            } catch (java.text.ParseException pe) {}
            int nbGen = (int) sp.getValue();
            fenAFermer.dispose();
            source.faireNStep(nbGen);
        }
    }
    
    public class ResetListener implements ActionListener{
        
        private Plateau source;
        
        @Override
        public void actionPerformed(ActionEvent e) 
        {
            source.reset();
        }
        
        public ResetListener(Plateau m)
        {
            source=m;
        }
    }
        
}
