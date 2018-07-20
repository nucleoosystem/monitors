result = {
    "type": "line",
    "data": None,
    "options": {
        "responsive": True,
        "title":{
            "display":True,
            "text":"Master: Replication Lag"
        },
        "tooltips": {
            "mode": "index",
            "intersect": False
        },
        "hover": {
            "mode": "nearest",
            "intersect": True
        },
        "scales": {
            "xAxes": [{
                "display": True,
                "scaleLabel": {
                    "display": True,
                    "labelString": "Time"
                }
            }],
            "yAxes": [{
                "display": True,
                "scaleLabel": {
                    "display": True,
                    "labelString": "Size (MB)"
                },
                "ticks": {
                    "beginAtZero": True
                }
            }]
        }
    }
}
