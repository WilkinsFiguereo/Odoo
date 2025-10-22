from odoo import models, fields, api
from odoo.exceptions import ValidationError

class UserTask(models.Model):
    _name = 'user.task'
    _description = 'User Task'
    _order = 'deadline asc'
    
    name = fields.Char(string='Titulo', required=True)
    description = fields.Text(string='Descripcion') 
    priority = fields.Selection([('0', 'Baja'), ('1', 'Media'), ('2', 'Alta')] , string='Prioridad', default='1', required=True)
    state = fields.Selection([('draft', 'Borrador'), ('in_progress', 'En Progreso'), ('done', 'Hecho')] , string='Estado', default='draft', required=True)
    deadline = fields.Date(string='Fecha Limite', required=True)
    is_done = fields.Boolean(string='Hecho', default=False, compute='_compute_is_done', store=True)
    user_id = fields.Many2one('res.users', string='Asignado a', default=lambda self: self.env.user, required=True)
    
    @api.depends('state')
    def _compute_is_done(self):
        for record in self:
            record.is_done = (record.state == 'done')
            
    @api.constrains('deadline')
    def _check_deadline(self):
        for task in self:
            if task.deadline < fields.Date.today():
                raise ValidationError("La fecha limite no puede ser en el pasado.")
        