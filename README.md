# Power and BTU monthly report dashboard

**1. Import Data from monthly and daily report in .csv file**

**2. Have 5 plotly graph in dash board** <br />
&nbsp;&nbsp;&nbsp;&nbsp;2.1 def kW_each_power_meter_month(dg): --> Area plot of kW from each power meter<br />
&nbsp;&nbsp;&nbsp;&nbsp;2.2 line plot kW of each power meter with tab selection <br />
&nbsp;&nbsp;&nbsp;&nbsp;2.3 def pie_plot_kW_TR_month(dg): --> pie plot of kW from each power meter <br />
&nbsp;&nbsp;&nbsp;&nbsp;2.4 def create_box_plot_month(dg): --> box plot of kW form each power meter <br />
&nbsp;&nbsp;&nbsp;&nbsp;2.5 def summary_month: --> plotly table included kW_mean, kW_max and kW_total from each power meter<br />

**3. Create dashboard on dash**

**4. Lay out of dash board is** <br />
&nbsp;&nbsp;&nbsp;&nbsp;Row1 : Col1 is Title <br /> 
&nbsp;&nbsp;&nbsp;&nbsp;Row2 : (Col1 is def kW_each_power_meter_month(dg):, Col2 is line plot kW of each power meter with tab selection) <br />
&nbsp;&nbsp;&nbsp;&nbsp;Row3 : (Col1 is def pie_plot_kW_TR_month(dg):, Col2 is def create_box_plot_month(dg):) <br />
&nbsp;&nbsp;&nbsp;&nbsp;Row4 : Col1 is summary_month:

**5. Deploy by Render**
