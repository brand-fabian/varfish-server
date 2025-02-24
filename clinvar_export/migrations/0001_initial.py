# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-30 13:17
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("variants", "0079_auto_20210204_1006"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssertionMethod",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("is_builtin", models.BooleanField(default=False)),
                ("title", models.TextField(max_length=200)),
                ("reference", models.TextField(max_length=200)),
            ],
            options={"ordering": ("reference",),},
        ),
        migrations.CreateModel(
            name="Family",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("case_name", models.TextField(max_length=128)),
                (
                    "pedigree",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=list, help_text="Pedigree information.", null=True
                    ),
                ),
                (
                    "case",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="variants.Case",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="variants.CaseAwareProject"
                    ),
                ),
            ],
            options={"ordering": ("date_created",),},
        ),
        migrations.CreateModel(
            name="Individual",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("name", models.TextField(max_length=128)),
                ("taxonomy_id", models.IntegerField(default=9606)),
                ("sex", models.TextField(default="unknown", max_length=100)),
                ("affected", models.TextField(default="unknown", max_length=100)),
                (
                    "family",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clinvar_export.Family"
                    ),
                ),
            ],
            options={"ordering": ("date_created",),},
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("clinvar_id", models.IntegerField()),
                ("name", models.TextField()),
            ],
            options={"ordering": ("clinvar_id",),},
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("sort_order", models.IntegerField()),
                ("record_status", models.TextField(default="novel", max_length=32)),
                ("release_status", models.TextField(default="public", max_length=32)),
                ("significance_status", models.TextField(max_length=100)),
                ("significance_description", models.TextField(max_length=100)),
                ("significance_last_evaluation", models.DateField()),
                ("inheritance", models.TextField(blank=True, max_length=100, null=True)),
                ("age_of_onset", models.TextField(blank=True, max_length=100, null=True)),
                ("variant_assembly", models.TextField(max_length=64)),
                ("variant_chromosome", models.TextField(max_length=64)),
                ("variant_type", models.TextField(default="Variation", max_length=100)),
                ("variant_start", models.IntegerField(blank=True, null=True)),
                ("variant_stop", models.IntegerField(blank=True, null=True)),
                ("variant_reference", models.TextField(blank=True, null=True)),
                ("variant_alternative", models.TextField(blank=True, null=True)),
                (
                    "variant_gene",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(max_length=64), size=None
                    ),
                ),
                (
                    "variant_hgvs",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(), size=None
                    ),
                ),
                (
                    "diseases",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=list, null=True
                    ),
                ),
                (
                    "assertion_method",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clinvar_export.AssertionMethod",
                    ),
                ),
            ],
            options={"ordering": ("sort_order",),},
        ),
        migrations.CreateModel(
            name="SubmissionIndividual",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("sort_order", models.IntegerField()),
                (
                    "phenotypes",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=list, null=True
                    ),
                ),
                ("variant_origin", models.TextField(default="not-reported", max_length=100)),
                ("variant_allele_count", models.IntegerField(blank=True, default=None, null=True)),
                (
                    "variant_zygosity",
                    models.TextField(blank=True, default="not provided", max_length=100, null=True),
                ),
                ("source", models.TextField(max_length=100)),
                (
                    "citations",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(max_length=100),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                ("tissue", models.TextField(blank=True, max_length=100, null=True)),
                (
                    "individual",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clinvar_export.Individual"
                    ),
                ),
                (
                    "submission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submission_individuals",
                        to="clinvar_export.Submission",
                    ),
                ),
            ],
            options={"ordering": ("sort_order",),},
        ),
        migrations.CreateModel(
            name="SubmissionSet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("state", models.TextField(max_length=32)),
                ("title", models.TextField()),
            ],
            options={"ordering": ("date_created",),},
        ),
        migrations.CreateModel(
            name="Submitter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                ("clinvar_id", models.IntegerField()),
                ("name", models.TextField()),
            ],
            options={"ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="SubmittingOrg",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now_add=True, help_text="DateTime of creation"),
                ),
                (
                    "date_modified",
                    models.DateTimeField(auto_now=True, help_text="DateTime of last modification"),
                ),
                ("sort_order", models.IntegerField()),
                (
                    "sodar_uuid",
                    models.UUIDField(default=uuid.uuid4, help_text="SODAR UUID", unique=True),
                ),
                (
                    "organisation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clinvar_export.Organisation",
                    ),
                ),
                (
                    "submission_set",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submitting_orgs",
                        to="clinvar_export.SubmissionSet",
                    ),
                ),
            ],
            options={"ordering": ("sort_order",),},
        ),
        migrations.AddField(
            model_name="submissionset",
            name="organisations",
            field=models.ManyToManyField(
                through="clinvar_export.SubmittingOrg", to="clinvar_export.Organisation"
            ),
        ),
        migrations.AddField(
            model_name="submissionset",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="variants.CaseAwareProject"
            ),
        ),
        migrations.AddField(
            model_name="submissionset",
            name="submitter",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="submission_sets",
                to="clinvar_export.Submitter",
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="individuals",
            field=models.ManyToManyField(
                through="clinvar_export.SubmissionIndividual", to="clinvar_export.Individual"
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="submission_set",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="submissions",
                to="clinvar_export.SubmissionSet",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="submittingorg", unique_together=set([("organisation", "submission_set")]),
        ),
        migrations.AlterUniqueTogether(
            name="submissionindividual", unique_together=set([("individual", "submission")]),
        ),
        migrations.AlterUniqueTogether(
            name="family", unique_together=set([("case_name", "project")]),
        ),
    ]
