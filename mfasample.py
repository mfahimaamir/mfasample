import numpy as np
import os
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
import matplotlib.pyplot as plt
import numpy
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from st_aggrid import JsCode, AgGrid, GridOptionsBuilder
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
from st_aggrid.shared import GridUpdateMode

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import pandas as pd
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder



import numpy
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np





st.html("""
    <style>
        .stMainBlockContainer {
            max-width:350rem;
            max-hight:10rem;
        }
    </style>
    """
)



#url12 = "https://docs.google.com/spreadsheets/d/1TrljfQUEw2cEiYUOyXXfH7u0VF0IDARZ/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
#url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
url12 = "https://docs.google.com/spreadsheets/d/1j4zRBnAb1nXi4NMMC8NEnEZMBVTW2oje/edit?pli=1&gid=92713901#gid=92713901"
file_id122 = url12.split("/")[-2]
path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
iqradata = pd.read_excel(path1122)

        #st.write(st.session_state.df92 )
        #datag = st.session_state.df92


#@st.cache_data()
def load_data():
    #data = pd.read_excel("C:/mfa/exportpv.xlsx")
    #data = pd.read_excel('c:\mfa\iqradata.xlsx')
    data= iqradata
    #data = pd.read_csv("./data.csv", parse_dates=["referenceDate"])
    return data

data = load_data()



shouldDisplayPivoted = st.checkbox("Pivot data on Reference Date",True)
tab1, tab2, tab3, tab4 , tab5, tab6, tab7,tab8,tab9,tab10,tab11 = st.tabs(["View-1", "View-2", "View-3", "View-4", "View-5", "View-6", "View-7", "View-Graph", "View-Groupby", "View-Pivot", "View-Finance"])
#tab1, tab2, tab3, tab4 = st.tabs(["View-1", "View-2", "View-3", "View-4"])

with tab1:
#with st.expander("Pivot -1 "):
    gb = GridOptionsBuilder()

    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gb.configure_column(
        field="Campus", header_name="Campus", width=80, rowGroup=shouldDisplayPivoted
    )

    gb.configure_column(
        field="Faculty",
        header_name="Faculty",
        flex=1,
        tooltipField="Faculty",
        rowGroup=shouldDisplayPivoted,
        #rowGroup=True if shouldDisplayPivoted else False,
    )
    gb.configure_column(
        field="Career",
        header_name="Career",
        width=110,
        rowGroup=shouldDisplayPivoted,
    )

    #Campus	Faculty	Career	Program	ctype	semister	credithh		
    gb.configure_column(
        field="Program",
        header_name="Program",
        width=150,
        tooltipField="Program",
        rowGroup=shouldDisplayPivoted,
    )
    gb.configure_column(
        field="ctype",
        header_name="ctype",
        width=150,
        tooltipField="ctype",
        rowGroup=shouldDisplayPivoted,
    )

    #field="dat32 ReferenceDate",
    #valueGetter="new Date(data.referenceDate).getFullYear()",
    gb.configure_column(
        field="semister",
        header_name="semister",
        #valueGetter="ctype",
        valueGetter="(data.semister)",
        pivot=True,
        hide=True,
    )


    #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",

    gb.configure_column(
        field="credithh",
        #header_name="Volume [MWh]",
        header_name="credithh",
        width=100,
        type=["numericColumn"],
        aggFunc="sum",
        valueFormatter="value.toLocaleString()",
    )

    gb.configure_grid_options(
        tooltipShowDelay=0,
        pivotMode=shouldDisplayPivoted,
    )

    gb.configure_grid_options(
        autoGroupColumnDef=dict(
            minWidth=300, 
            pinned="left", 
            cellRendererParams=dict(suppressCount=True)
        )
    )
    go = gb.build()

    AgGrid(data, gridOptions=go, width =1900 ,height=400)
    
with tab2:
    gb = GridOptionsBuilder()

    gb.configure_default_column(
        resizable=True,
        filterable=True,
        sortable=True,
        editable=False,
    )
    gb.configure_column(
        field="Campus", header_name="Campus", width=80, rowGroup=shouldDisplayPivoted
    )

    gb.configure_column(
        field="Faculty",
        header_name="Faculty",
        flex=1,
        tooltipField="Faculty",
        rowGroup=shouldDisplayPivoted,
        #rowGroup=True if shouldDisplayPivoted else False,
    )
    gb.configure_column(
        field="Career",
        header_name="Career",
        width=110,
        rowGroup=shouldDisplayPivoted,
    )

    #Campus	Faculty	Career	Program	ctype	semister	credithh		
    gb.configure_column(
        field="Program",
        header_name="Program",
        width=150,
        tooltipField="Program",
        rowGroup=shouldDisplayPivoted,
    )
    
    #field="dat32 ReferenceDate",
    #valueGetter="new Date(data.referenceDate).getFullYear()",
    gb.configure_column(
        field="semister",
        header_name="semister",
        #valueGetter="ctype",
        valueGetter="(data.semister)",
        pivot=True,
        hide=True,
    )

    gb.configure_column(
            field="ctype",
            header_name="ctype",
            #valueGetter="ctype",
            valueGetter="(data.ctype)",
            pivot=True,
            hide=True,
        )

    #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",

    gb.configure_column(
        field="credithh",
        #header_name="Volume [MWh]",
        header_name="credithh",
        width=100,
        type=["numericColumn"],
        aggFunc="sum",
        valueFormatter="value.toLocaleString()",
    )

    gb.configure_grid_options(
        tooltipShowDelay=0,
        pivotMode=shouldDisplayPivoted,
    )

    gb.configure_grid_options(
        autoGroupColumnDef=dict(
            minWidth=300, 
            pinned="left", 
            cellRendererParams=dict(suppressCount=True)
        )
    )
    go = gb.build()

    AgGrid(data, gridOptions=go, width =1900 ,height=400)
with tab3:
    t = pivot_ui(data)

    with open(t.src) as t:
        components.html(t.read(), width=900, height=1000, scrolling=True)


with tab4:
    st.write(iqradata)
    table = pd.pivot_table(iqradata, values ='credithh', index =['Campus',	'Faculty',	'Career',	'Program'], 
                         columns =['ctype',	'semister'], aggfunc = np.sum) 
    st.header("=================Pivot -1=================== ")
    st.write(table)
    table1 = pd.pivot_table(iqradata, values ='credithh', index =['Campus',	'Faculty',	'Career',	'Program'], 
                         columns =['semister','ctype'], aggfunc = np.sum) 
    st.header("=================Pivot -2=================== ")
    st.write(table1)
    table2 = pd.pivot_table(iqradata, values ='credithh', index =['Campus',	'Faculty',	'Career',	'Program','ctype'], 
                         columns =['semister'], aggfunc = np.sum) 
    st.header("=================Pivot -3=================== ")
    st.write(table2)


with tab5:
#        'Campus',	'Faculty',	'Career',	'Program',	'ctype',	'semister'	credithh

    table3 = iqradata.groupby(['Campus',	'Faculty',	'Career',	'Program']).apply(lambda sub_df:
    sub_df.pivot_table(index=['ctype'],columns =['semister'], values=['credithh'], aggfunc='sum', margins=True))
    st.write(table3)
with tab6:
    dfg = pd.DataFrame(dict(
        Business='MUHAMMAD;FAHIM;AAMIR;Beauty & Spas;Burgers-Restaurants;Pizza;Mexican Restaurants;Modern European-Restaurants;Chineese'.split(';'),
        aniticipation=[0] * 9,
        enjoyment=[6., 1., 6., 33.,150., 19.5, 9, 43, 81],
        sad=[1., 2., 1., 3., 13.5, 3, 4, 2, 11],
        disgust=[1, 1, 0, 3, 37, 3, 89, 32, 41],
        anger=[1.5, 2.1, 4.2, 9.4, 19.3, 3.5, 3.8, 3, 1.7],
        surprise=[3, 0, 0, 2, 12, 1, 29, 32, 11],
        fear=[0, 1, 1, 9, 22, 1, 19, 52, 21],
        trust=[0] * 9
    ))

    st.write(dfg)
    fig, axes = plt.subplots(3, 3, figsize=(10, 6))
    #fig, axes = plt.subplots(2, 3, figsize=(10, 6))

    for i, (idx, row) in enumerate(dfg.set_index('Business').iterrows()):
        ax = axes[i // 3, i % 3]
        row = row[row.gt(row.sum() * .01)]
        ax.pie(row, labels=row.index, autopct='%1.1f%%',startangle=30)
        ax.set_title(idx)
        #plt.legend()
        

    fig.subplots_adjust(wspace=.2)

    st.pyplot(plt)

with tab7:
    
    data = {'Date': ['2024-03-05', '2024-03-06', '2024-03-07', '2024-03-08', '2024-03-09', '2024-03-10'],
            'Cost Price': [100, 120, 110, 1500, 1600, 1550],
            'Satisfaction Score': [90, 80, 70, 95, 85, 75],
            'Sales Amount': [1000, 800, 1200, 900, 1100, None]}

    df = pd.DataFrame(data)
    # Highlighting Maximum and Minimum Values
    dd5 = df.style.highlight_max(color='green', axis=0 , subset=['Cost Price', 'Satisfaction Score', 'Sales Amount']).highlight_min(color='red', axis=0 , subset=['Cost Price', 'Satisfaction Score', 'Sales Amount'])
    st.write(dd5)
    
  
            



with tab8:  # =======================================================================
    
    labels2 = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes2 = [15, 30, 45, 10]
    #st.write(labels2)
    #st.write(sizes2)
    #def display_grid(df: pd.DataFrame):    
    data = {
        'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
        'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
        'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing'],
        'iTEM': ['TV', 'CAL', 'BUS', 'TRAIN', 'TANK', 'TABLE', 'DESK'],
        'Person': ['gggTV', 'dddCAL', 'ffffBUS', 'ssssTRAIN', 'ffffTANK', 'ssssTABLE', 'dddDESK'],
        'Sale': [76445, 45555, 73356, 54467, 65758, 544456, 75556],
        'Comm': [1726, 1425, 1725, 1527, 1628, 1426, 1276],
        'Qty': [765, 455, 756, 567, 678, 456, 756]
        
        }

    df = pd.DataFrame(data)


    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(
            selection_mode="multiple",
            #use_checkbox=True,
            pre_selected_rows=None,  # <-- Set to manually persist checkbox state
        )


            # Configure column filters for all columns
    for column in df.columns:
            gb.configure_column(column, filter=True)

    #gb.configure_grid_options(pivotMode= True)

    gridOptions = gb.build()
    mfa = AgGrid(
            df,
            gridOptions=gridOptions,
            update_mode=GridUpdateMode.GRID_CHANGED,
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
            data_return_mode=DataReturnMode.FILTERED   # <-- Gets filtered data, but not filters applied to columns
        )

    if st.button('Check availability'):
        mfa4 =mfa['data']
        selectedcol = mfa4.columns
    #   selectedcolgroup= selectedcol-1
        #allgroup = ''
    #    for column in  int(len(mfa4.columns))-1: 
    #       allgroup=allgroup+' '+mfa4[column].values.tolist()
            #gb.configure_column(column, filter=True)

    #  st.header(allgroup)
        fild = pd.DataFrame(mfa['columns_state'])
        above_35= fild["hide"] 
        above_36= fild["colId"] 
        list_from_df = above_36.values.tolist()
        list_from_column = fild["colId"].tolist()
        fild["hide"] = fild["hide"].astype(int) 
        fild = fild[fild["hide"]==0 ]
        list_from_df2 = fild["colId"].values.tolist()
        mfa5 = mfa4[list_from_column]
        mfa6 = mfa4[list_from_df2]
        colt = int(len(mfa6.columns)) 
        #df12 = df.groupby('Region')['Sale'].sum().reset_index()
        df12 = df.groupby(mfa6.columns[0])[mfa6.columns[colt-1]].sum().reset_index()
        st.write(df12)
        df12["expl"] = 0.1
        
        #s = df.groupby('text').agg({'word': list, 'num': 'count'}).reset_index()
    ## item= mfa6.iloc[:,[0]].values.tolist()
        
        colt2 = int(len(mfa6.columns))
        st.write(colt2)
        #item= mfa6.iloc[:,[0]].values.tolist()
        item = df12.columns[0]
        itemvalue  = df12[item].values.tolist()
        last2 = df12.columns[1]
        cost  = df12[last2].values.tolist()
        last1 = df12.columns[2]
        expl  = df12[last1].values.tolist()

        #cost= df.iloc[:,[colt-2]].values.tolist()
        #expl= df.iloc[:,[colt-1]].values.tolist()
        
        #st.write(mfa6)
        #st.write(colt)
        #st.write(item)
        #st.write(cost)
        #st.write(expl)








        fig1, ax1 = plt.subplots()
        ax1.pie(cost, explode=expl, labels=itemvalue, autopct='%1.1f%%',        shadow=True, startangle=90)
        #ax1.pie(sizes, explode=explode, labels=item, autopct='%1.1f%%',        shadow=True, startangle=90)
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

        
        fig1 = px.pie(df12, values=last2, names=item, title='Pie Chart of Languages')      #plotly pie차트
        st.plotly_chart(fig1)

        fig2 = px.bar( df12, x=item, y=last2)        #plotly bar차트
        st.plotly_chart(fig2)
        
        counts = pd.Series(cost, 
                    index=itemvalue)
        colors = ['#191970', '#001CF0', '#0038E2', '#0055D4', '#0071C6', '#008DB8', '#00AAAA',
            '#00C69C', '#00E28E', '#00FF80', ]
        explode = expl

        counts.plot(kind='pie', fontsize=17, colors=colors, explode=explode)
    #   plt.axis('equal')
        plt.ylabel('Muhammad is the best')
        #plt.legend(labels=itemvalue, loc="best")
        #plt.show()
        st.pyplot(plt)    
    #counts.index
        
        #cost  = df['cost'].values.tolist()
        #expl  = df['expl'].values.tolist()
    #listxx= mfa6.iloc[:,[colt-1]].values.tolist()


        #listyy= mfa6.iloc[:,[0]].values.tolist()
        #listyy= mfa6.iloc[:,[0]].T.values.tolist()
        
        #Third_Column=DF.iloc[:,2]
        #colname = df.columns[2]
        #listyy0= (df.to_string(index=False))
    #   listyy=listyy0.values.tolist()
    #   colt = int(len(mfa6.columns))
        #listxx= mfa6.iloc[:,[colt-1]].values.tolist()
    #    listxx= mfa6.iloc[:,[colt-1]].astype('int').T.values.tolist()
        
        
        #test.to_numpy('int').tolist()
        #test.T.values.tolist()
    #  st.write(listyy)
        

        
    #    plt.barh(itemvalue,cost)
        #plt.show()
        
        #plt.bar(cost,itemvalue , color='skyblue')
    #   plt.xlabel('Visualization Library')
    #  plt.ylabel('Number of Enthusiasts')
    # plt.title('Which Visualization Library Do People Prefer?')
        #plt.show()
        #st.pyplot(plt)
        #st.header(len(mfa6.columns)-1)
        with st.expander("Filter Column and Row with Grahp"):
            
            #mfa6
            #st.write( mfa6)
            
            allgroup = mfa6
            tofiled= len(mfa6.columns)-1
            #st.header(tofiled)
            #tofiled=tofiled-
            
            ttt= int(tofiled)
            
            expl= ''
            lastcol = int(len(mfa6.columns)-1)
            lastcol2 = mfa6.columns[lastcol]
            #st.write(lastcol)
            #sumcoll  = df[lastcol2]

            if lastcol==2:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
            #   st.write(len(mfa6.columns)-1)
            #   st.write(mfa6['groupfield'])
            if lastcol==3:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                last3 = mfa6.columns[2]
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last3].values.tolist()
            #  st.write(len(mfa6.columns)-1)
            # st.write(mfa6['groupfield'])
            if lastcol==4:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                last3 = mfa6.columns[2]
                last4 = mfa6.columns[3]
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last3].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last4].values.tolist()
                #st.write(len(mfa6.columns)-1)
                #st.write(mfa6['groupfield'])
                
            if lastcol==5:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                last3 = mfa6.columns[2]
                last4 = mfa6.columns[3]
                last5 = mfa6.columns[4]
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last3].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last4].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last5].values.tolist()
                #st.write(len(mfa6.columns)-1)
                #st.write(mfa6['groupfield'])
            if lastcol==6:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                last3 = mfa6.columns[2]
                last4 = mfa6.columns[3]
                last5 = mfa6.columns[4]
                last6 = mfa6.columns[5]
                #st.header(len(mfa6.columns)-1)
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last3].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'' + mfa6[last4].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' + mfa6[last5].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' + mfa6[last6].values.tolist()
                #st.write(len(mfa6.columns)-1)
                #st.write(mfa6['groupfield'])
            if lastcol==7:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                last3 = mfa6.columns[2]
                last4 = mfa6.columns[3]
                last5 = mfa6.columns[4]
                last6 = mfa6.columns[5]
                last7 = mfa6.columns[6]
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last3].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last4].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last5].values.tolist()
                #mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last6].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last7].values.tolist()
                #st.write(len(mfa6.columns)-1)
                #st.write(mfa6['groupfield'])
            if lastcol==8:
                last1 = mfa6.columns[0]
                last2 = mfa6.columns[1]
                last3 = mfa6.columns[2]
                last4 = mfa6.columns[3]
                last5 = mfa6.columns[4]
                last6 = mfa6.columns[5]
                last7 = mfa6.columns[6]
                last8 = mfa6.columns[7]
                mfa6['groupfield']=mfa6[last1].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last2].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last3].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last4].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last5].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last6].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last7].values.tolist()
                mfa6['groupfield']=mfa6['groupfield']+'/' +mfa6[last8].values.tolist()
                #st.write(len(mfa6.columns)-1)
                #st.write(mfa6['groupfield'])
            
            
            df15 =mfa6[['groupfield',lastcol2]]
            #st.write(df15)
            
            
            fl = df15.columns[0]
            f2 = df15.columns[1]
            #st.write(lastcol2)
            df16 = df15.groupby(fl)[f2].sum().reset_index()
            #df2 = df.groupby('Courses').sum()
            st.write(df16)
            df16["expl"] = 0.1
            #st.write(df16)
            
            item = df16.columns[0]
            itemvalue  = df16[item].values.tolist()
            last2 = df16.columns[1]
            cost  = df16[last2].values.tolist()
            last1 = df16.columns[2]
            expl  = df16[last1].values.tolist()

            fig1, ax1 = plt.subplots()
            ax1.pie(cost, explode=expl, labels=itemvalue, autopct='%1.1f%%',        shadow=True, startangle=90)
            #ax1.pie(sizes, explode=explode, labels=item, autopct='%1.1f%%',        shadow=True, startangle=90)
            #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',        shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)

        with st.expander("Iqra Dynamic Graph"):
            
            #df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
            df = pd.read_excel('c:/mfa/iqradata.xlsx')
            
            #df['newf'] = df['type']+'-'+df['shelf']
            
            st.write(df)
    #        Campus	Faculty	Career	Program	ctype	semister	credithh
    #        'Campus','Faculty','Career','Program','ctype','semister'	credithh


            fig = px.sunburst(df, path=['Campus','Faculty','Career','Program','ctype','semister'], values='credithh')
            #fig = px.sunburst(df, path=['mfr','shelf','type'], values='cereal')
            #fig.show()
            st.plotly_chart(fig)
            

            
        with st.expander("Dynamic Graph"):
            
            df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
            #df = pd.read_csv('c:/mfa/piedata2.csv')
            df['newf'] = df['type']+'-'+df['shelf']
            st.write(df)


            fig = px.sunburst(df, path=['mfr','newf','shelf','type'], values='cereal')
            #fig = px.sunburst(df, path=['mfr','shelf','type'], values='cereal')
            #fig.show()
            st.plotly_chart(fig)


            #piechart5 ============================

            data2 = {
                'ctry': ['USA', 'PHI', 'CHN'],
                'area': ['Karachi', 'Mirput', 'Multan'],
                'person': ['dfgdfg', 'dfghfh', 'fhfghf'],
                'item': ['computer', 'cdrome', 'airoplan'],
                'customer': ['cffffffr', 'csssss', 'afffff'],
                
                'gold': [12, 1, 20,],
                'silver': [4,4, 12],
                'bronze': [8, 2, 30],
                'Iron': [55, 32, 36],
                'sum': [24, 657, 5662]
            }


            data = {
                'ctry': ['USA', 'PHI', 'CHN'],
                'gold': [12, 1, 20,],
                'silver': [4,4, 12],
                'bronze': [8, 2, 30],
                'sum': [24, 657, 5662]
            }

            df = pd.DataFrame(data)
            st.dataframe(df)

            cols = st.columns([1, 1])

            with cols[0]:
                medal_type = st.selectbox('Medal Type', ['gold', 'silver', 'bronze'])
                
                fig = px.pie(df, values=medal_type, names='ctry',
                            title=f'number of {medal_type} medals',
                            height=300, width=200)
                fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
                st.plotly_chart(fig, use_container_width=True)

            with cols[1]:
                st.text_input('sunburst', label_visibility='hidden', disabled=True)
                #fig = px.sunburst(df, path=['ctry','area', 'person', 'item', 'customer'],
                fig = px.sunburst(df, path=['ctry', 'gold', 'silver', 'bronze'],
                                values='sum', height=300, width=200)
                fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
                st.plotly_chart(fig, use_container_width=True)
            
            
            
            #with cols[1]:
            #    st.text_input('sunburst', label_visibility='hidden', disabled=True)
            #  #fig = px.sunburst(df, path=['ctry','area', 'person', 'item', 'customer'],
            #   fig = px.sunburst(df, path=['ctry', 'gold', 'silver', 'bronze'],
            #                  values='sum', height=300, width=200)
            #  fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
            #  st.plotly_chart(fig, use_container_width=True)

with tab9:  # =======================================================================
    url12 = "https://docs.google.com/spreadsheets/d/1aGT703zXe1h_dgG-59fHlFEYzNdYqyla/edit?gid=1489174106#gid=1489174106"
    file_id122 = url12.split("/")[-2]
    path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
    df = pd.read_excel(path1122)

    mfa = pd.concat([
            df.assign(
                **{x: 'Total' for x in 'abc'[i:]}
            ).groupby(list('abc')).sum() for i in range(4)
        ]).sort_index()

    st.write(mfa)

    mfa1= pd.concat([
            df.assign(
                **{x: '' for x in 'abc'[i:]}
            ).groupby(list('abc')).sum() for i in range(1, 4)
        ]).sort_index()

    st.write(mfa1)
with tab10:  # =======================================================================    
        df2 = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                        'position': ['G', 'G', 'F', 'F', 'G', 'F', 'F', 'F'],
                        'all_star': ['Y', 'N', 'Y', 'Y', 'N', 'N', 'N', 'Y'],
                        'area': ['ddY', 'ssN', 'ffY', 'ssY', 'ffN', 'ssN', 'ffN', 'ffY'],
                        'reg': ['ddsdY', 'sddsN', 'fssfY', 'sffsY', 'fssfN', 'ffssN', 'fssfN', 'ffY'],
                        'per': ['ddddY', 'sddsN', 'fddfY', 'sddsY', 'fddfN', 'sddsN', 'fddfN', 'ffY'],
                        'points': [4, 4, 6, 8, 9, 5, 5, 12]})

        #view DataFrame


        url12 = "https://docs.google.com/spreadsheets/d/1aGT703zXe1h_dgG-59fHlFEYzNdYqyla/edit?gid=1489174106#gid=1489174106"
        file_id122 = url12.split("/")[-2]
        path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
        df = pd.read_excel(path1122)

    
        #df = pd.read_excel('c:\mfa\mfatt.xlsx')


        ttt = pd.concat([
                df.assign(
                    **{x: 'Total' for x in 'abc'[i:]}
                ).groupby(list('abc')).sum() for i in range(4)
            ]).sort_index()

        #print(ttt)

        mya2 = pd.pivot_table(df2, values='points',
                                    index=['team', 'all_star'],
                                    columns=['position','area','per','reg'],
                                    aggfunc='sum')
        st.write(mya2)
        
        csv = mya2.to_csv().encode("utf-8")
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:",)
                    
with tab11:  # =======================================================================    
    st.markdown(
                """
                <style>
                [data-testid="stSidebar"] {
                    visibility: visible;
                }
                </style>
                """,
                unsafe_allow_html=True
                )
    #https://docs.google.com/spreadsheets/d/1xuKMK5ImclIZvlQ2CuTWbUOmkpu8i61H/edit?gid=1845779531#gid=1845779531
    url12 = "https://docs.google.com/spreadsheets/d/1xuKMK5ImclIZvlQ2CuTWbUOmkpu8i61H/edit?gid=1845779531#gid=1845779531"
    file_id122 = url12.split("/")[-2]
    path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122

    df5 = pd.read_excel(path1122)
    #df5 = pd.read_excel('c:/pytest/adata.xlsx')

    url123 = "https://docs.google.com/spreadsheets/d/1wtgtcEEruAN87dvFdKRVmTz_Q8KlywRa/edit?gid=1428546576#gid=1428546576"
    file_id1223 = url123.split("/")[-2]
    path1123 = "https://drive.google.com/uc?export=download&id=" + file_id1223
    df6 = pd.read_excel(path1123)
    #https://docs.google.com/spreadsheets/d/1xuKMK5ImclIZvlQ2CuTWbUOmkpu8i61H/edit?gid=1731351115#gid=1731351115
    #df6 = pd.read_excel('c:/mfa/vtable.xlsx')
    #df3  = pd.read_excel("c:\pytest\adata.xlsx")
    #st.write(df6)
    #t.sidebar(visibility=False) 
    #st.sidebar(visibility=True) 
    def GetLastName(row):
        nsarr = row['orgHierarchy'].split('|')
        return(nsarr[len(nsarr)-1])

    df=pd.DataFrame({ "orgHierarchy": ['01', 
                                    '01|01',
                                    '01|01|02',
                                    '01|01|02|01',
                                    '01|01|02|01|02',
                                    '01|01|02|01|03',
                                    '01|01|02|02',
                                    '01|01|03',
                                    '01|01|03|01',
                                    '01|01|03|02',
                                    '01|01|03|03',
                                    '01|01|03|04'],
                    "fullcode": ['01', 
                                    '01|01',
                                    '01|01|02',
                                    '01|01|02|01',
                                    '01|01|02|01|02',
                                    '01|01|02|01|03',
                                    '01|01|02|02',
                                    '01|01|03',
                                    '01|01|03|01',
                                    '01|01|03|02',
                                    '01|01|03|03',
                                    '01|01|03|04'],
                    "empname": [ 'ffffCEO', 'fffdddExec', 'dddffdsfdsf', 'sdfsdgdfg', 'fghgfhfgh',
                                    'fghfghdfg', 'ghfhughjghj', 'tytryrty', 'fghfghfghs', 'hdfgdfg',
                                    'fghfghfgh', 'jgjhgjghjffd' ], 
                    "jobTitle": [ 'CEO', 'Exec. Vice President', 'Director of Operations', 'Fleet Coordinator', 'Parts Technician',
                                    'Service Technician', 'Inventory Control', 'VP Sales', 'Sales Manager', 'Sales Executive',
                                    'Sales Executive', 'Sales Executive' ], 
                    "recid": [ 21, 22, 24, 222, 223,
                                    224,225, 226, 227, 228,
                                    229,220 ], 
                    
                    "employmentType": [ 'Permanent', 'Permanent', 'Permanent', 'Permanent', 'Contract', 'Contract', 'Permanent', 'Permanent',
                                        'Permanent', 'Contract', 'Contract', 'Permanent' ]}, 
    )

    df['Name'] = df.apply(lambda row: GetLastName(row), axis=1)
    df.insert(0, "Name", df.pop("Name"))    # move col to 0 pstn

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection(selection_mode="single", use_checkbox=False)
    gb.configure_column("orgHierarchy", hide = "True")
    gb.configure_column("Name", hide = "True")
    gridOptions = gb.build()

    gridOptions["autoGroupColumnDef"]= {'cellRendererParams': {'checkbox': True }}
    gridOptions["treeData"]=True     
    #gridOptions["treeData"]=True      #if off did not show the tree view 
    gridOptions["animateRows"]=True
    gridOptions["groupDefaultExpanded"]= -1   # expand all
    gridOptions["getDataPath"]=JsCode("function(data){ return data.orgHierarchy.split('|'); }").js_code

    dta = AgGrid(df, gridOptions=gridOptions, height=350, allow_unsafe_jscode=True, enable_enterprise_modules=True,     
                update_mode=GridUpdateMode.SELECTION_CHANGED)

    #st.write(dta['selected_rows'])
    mm=dta['selected_rows']
    #item1 = mm[1]
    mfa= pd.DataFrame(dta['selected_rows'])
    #st.write(mm)
    length = len(mm)
    if length>0 :
    #st.write(mfa["fullcode"][0])
        df7 = df5 
        filtered_df = df5[df5['code'] == mfa["fullcode"][0]]
    #st.write(filtered_df)
        gb5 = GridOptionsBuilder.from_dataframe(filtered_df)
        gb5.configure_selection(selection_mode="single")
        gb5.configure_side_bar()
        gridOptions5 = gb5.build()
        data2 = AgGrid(filtered_df,
                    gridOptions=gridOptions5,
                    enable_enterprise_modules=True,
                    allow_unsafe_jscode=True,
                    update_mode=GridUpdateMode.SELECTION_CHANGED,
                    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)
        mfahh= pd.DataFrame(data2['selected_rows'])
        length2 = len(mfahh)
        if length2>0 :
            #st.header("Muhammad is the best")
            #st.write(mfahh)
            #result = df3.loc[(df3[st.session_state.mfadd1] == st.session_state.mfa1) & (df3[mfadd2] == mfa2)]
            vsv1=mfahh["code"][0]
            vsv2=mfahh["mvid"][0]
            #st.write(vsv2)
            # acode,mvid,dvid
            #resultv = df6.loc[(df6["acode"] == vsv1) & (df6["mvid"] == vsv2)]
            resultv = df6.loc[df6["mvid"] == vsv2]
            #resultv = df6.loc[df6["acode"] == mfahh["code"][0]]
            #v_df = df6[df6['acode'] == mfahh["code"][0]]
            st.write(resultv)
                
            
            
            
            
            
            
            
            
            
            
            


                                    
