Attribute VB_Name = "Module1"
Sub StockDataEasy()

'Declare variables
Dim Ticker As String
Dim Summary_Table_Row As Double
Dim last_row As Double
Dim ticker_total As Double
Dim Worksheet As String
  
ticker_total = 0
Summary_Table_Row = 2
 
    For Each ws In Worksheets
    
        Cells(1, 8).Value = "Ticker"
        Cells(1, 9).Value = "Total Stock Volume"
     
        last_row = ws.Cells(Rows.Count, 1).End(xlUp).Row
        Worksheet = ws.Name
        ws.Activate
        
        For i = 2 To last_row

            Ticker = ws.Cells(i, 7).Value
        
            ticker_total = ticker_total + Ticker
            
                If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                
                Ticker = ws.Cells(i, 1).Value

                ws.Range("H" & Summary_Table_Row).Value = Ticker
              
                ws.Range("I" & Summary_Table_Row).Value = ticker_total
                      
                Summary_Table_Row = Summary_Table_Row + 1
                
                ticker_total = 0

            End If
        Next i
    Next ws
End Sub

