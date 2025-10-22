{
    'name': 'User Task Manager',
    'version': '1.0',
    'author': 'Cybrosys Technologies',
    'category': 'Productivity',
    'website': 'https://www.cybrosys.com',
    'summary': 'User Task Manager',
    'description': 'Practica creacion de modulo. Gestor de tareas.',
    'author': 'Wilkins',
    'depends': ['base'],
    'data': [
        'security/task_security.xml',
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'user_task_manager/static/src/css/task_kanban.css',
        ],
    },
}