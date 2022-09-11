<html>
      <head>
        <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        <py-env>
          - numpy
          - matplotlib
        </py-env>
      </head>
    
      <body>
        <h1>Plotting a histogram of Standard Normal distribution</h1>
        <div id="plot"></div>
        <py-script output="plot">
    import matplotlib.pyplot as plt
    import numpy as np
    
    np.random.seed(42)
    
    rv = np.random.standard_normal(1000)
    
    fig, ax = plt.subplots()
    ax.hist(rv, bins=30)
    fig
    
        </py-script>
      </body>
    </html>
  <!-- https://towardsdatascience.com/pyscript-unleash-the-power-of-python-in-your-browser-6e0123c6dc3f -->
