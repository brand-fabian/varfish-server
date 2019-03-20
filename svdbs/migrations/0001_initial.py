# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-23 09:52
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DbVarSv",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("bin", models.IntegerField(default=0)),
                (
                    "containing_bins",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("num_carriers", models.IntegerField()),
                ("sv_type", models.CharField(max_length=1024)),
                ("method", models.CharField(max_length=1024)),
                ("analysis", models.CharField(max_length=1024)),
                ("platform", models.CharField(max_length=1024)),
                ("study", models.CharField(max_length=1024)),
                (
                    "clinical_assertions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1024), size=None
                    ),
                ),
                (
                    "clinvar_accessions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1024), size=None
                    ),
                ),
                ("bin_size", models.CharField(max_length=32)),
                ("min_ins_length", models.IntegerField(blank=True, null=True)),
                ("max_ins_length", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DgvGoldStandardSvs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start_outer", models.IntegerField()),
                ("start_inner", models.IntegerField()),
                ("end_inner", models.IntegerField()),
                ("end_outer", models.IntegerField()),
                ("bin", models.IntegerField(default=0)),
                (
                    "containing_bins",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("accession", models.CharField(max_length=32)),
                ("sv_type", models.CharField(max_length=8)),
                (
                    "sv_sub_type",
                    models.CharField(
                        choices=[
                            ("gain", "gain"),
                            ("loss", "loss"),
                            ("gain+loss", "gain+loss"),
                            ("insertion", "insertion"),
                            ("novel sequence insertion", "novel sequence insertion"),
                            ("deletion", "deletion"),
                            ("complex", "complex"),
                            ("sequence alteration", "sequence alteration"),
                        ],
                        max_length=8,
                    ),
                ),
                ("num_studies", models.IntegerField()),
                (
                    "studies",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=128), size=None
                    ),
                ),
                ("num_platforms", models.IntegerField()),
                (
                    "platforms",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=128), size=None
                    ),
                ),
                ("num_algorithms", models.IntegerField()),
                (
                    "algorithms",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=128), size=None
                    ),
                ),
                ("num_variants", models.IntegerField()),
                ("num_carriers", models.IntegerField()),
                ("num_unique_samples", models.IntegerField()),
                ("num_carriers_african", models.IntegerField()),
                ("num_carriers_asian", models.IntegerField()),
                ("num_carriers_european", models.IntegerField()),
                ("num_carriers_mexican", models.IntegerField()),
                ("num_carriers_middle_east", models.IntegerField()),
                ("num_carriers_native_american", models.IntegerField()),
                ("num_carriers_north_american", models.IntegerField()),
                ("num_carriers_oceania", models.IntegerField()),
                ("num_carriers_south_american", models.IntegerField()),
                ("num_carriers_admixed", models.IntegerField()),
                ("num_carriers_unknown", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="DgvSvs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("bin", models.IntegerField(default=0)),
                (
                    "containing_bins",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("accession", models.CharField(max_length=32)),
                ("sv_type", models.CharField(max_length=32)),
                (
                    "sv_sub_type",
                    models.CharField(
                        choices=[
                            ("gain", "gain"),
                            ("loss", "loss"),
                            ("gain+loss", "gain+loss"),
                            ("insertion", "insertion"),
                            ("novel sequence insertion", "novel sequence insertion"),
                            ("deletion", "deletion"),
                            ("complex", "complex"),
                            ("sequence alteration", "sequence alteration"),
                        ],
                        max_length=32,
                    ),
                ),
                ("study", models.CharField(max_length=128)),
                (
                    "platform",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=128), size=None
                    ),
                ),
                ("num_samples", models.IntegerField()),
                ("observed_gains", models.IntegerField()),
                ("observed_losses", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ExacCnv",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("bin", models.IntegerField(default=0)),
                (
                    "containing_bins",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("sv_type", models.CharField(max_length=32)),
                (
                    "population",
                    models.CharField(
                        choices=[
                            ("AFR", "African"),
                            ("AMR", "American"),
                            ("EAS", "East Asian"),
                            ("FIN", "Finnish"),
                            ("NFE", "Non-Finish European"),
                            ("OTH", "Other"),
                            ("SAS", "South Asian"),
                        ],
                        max_length=3,
                    ),
                ),
                ("phred_score", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="GnomAdSv",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("bin", models.IntegerField(default=0)),
                (
                    "containing_bins",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("ref", models.CharField(default="N", max_length=64)),
                (
                    "alt",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), default=[], size=None
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("svtype", models.CharField(max_length=64)),
                ("svlen", models.IntegerField()),
                (
                    "filter",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "evidence",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=8), size=None
                    ),
                ),
                (
                    "algorithms",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=32), size=None
                    ),
                ),
                ("chr2", models.CharField(blank=True, max_length=32, null=True)),
                ("cpx_type", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "cpx_intervals",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), blank=True, null=True, size=None
                    ),
                ),
                ("source", models.CharField(blank=True, max_length=64, null=True)),
                ("strands", models.CharField(blank=True, max_length=2, null=True)),
                ("unresolved_type", models.CharField(blank=True, max_length=64, null=True)),
                ("pcrplus_depleted", models.BooleanField()),
                ("pesr_gt_overdispersion", models.BooleanField()),
                (
                    "protein_coding_lof",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_dup_lof",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_copy_gain",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_dup_partial",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_msv_exon_ovr",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_intronic",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_inv_span",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_utr",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                (
                    "protein_coding_nearest_tss",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                ("protein_coding_intergenic", models.BooleanField()),
                (
                    "protein_coding_promoter",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                ("an", models.IntegerField()),
                (
                    "ac",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "af",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=None
                    ),
                ),
                ("n_bi_genos", models.IntegerField()),
                ("n_homref", models.IntegerField()),
                ("n_het", models.IntegerField()),
                ("n_homalt", models.IntegerField()),
                ("freq_homref", models.FloatField()),
                ("freq_het", models.FloatField()),
                ("freq_homalt", models.FloatField()),
                ("popmax_af", models.FloatField()),
                ("afr_an", models.IntegerField()),
                (
                    "afr_ac",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "afr_af",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=None
                    ),
                ),
                ("afr_n_bi_genos", models.IntegerField()),
                ("afr_n_homref", models.IntegerField()),
                ("afr_n_het", models.IntegerField()),
                ("afr_n_homalt", models.IntegerField()),
                ("afr_freq_homref", models.FloatField()),
                ("afr_freq_het", models.FloatField()),
                ("afr_freq_homalt", models.FloatField()),
                ("amr_an", models.IntegerField()),
                (
                    "amr_ac",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "amr_af",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=None
                    ),
                ),
                ("amr_n_bi_genos", models.IntegerField()),
                ("amr_n_homref", models.IntegerField()),
                ("amr_n_het", models.IntegerField()),
                ("amr_n_homalt", models.IntegerField()),
                ("amr_freq_homref", models.FloatField()),
                ("amr_freq_het", models.FloatField()),
                ("amr_freq_homalt", models.FloatField()),
                ("eas_an", models.IntegerField()),
                (
                    "eas_ac",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "eas_af",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=None
                    ),
                ),
                ("eas_n_bi_genos", models.IntegerField()),
                ("eas_n_homref", models.IntegerField()),
                ("eas_n_het", models.IntegerField()),
                ("eas_n_homalt", models.IntegerField()),
                ("eas_freq_homref", models.FloatField()),
                ("eas_freq_het", models.FloatField()),
                ("eas_freq_homalt", models.FloatField()),
                ("eur_an", models.IntegerField()),
                (
                    "eur_ac",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "eur_af",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=None
                    ),
                ),
                ("eur_n_bi_genos", models.IntegerField()),
                ("eur_n_homref", models.IntegerField()),
                ("eur_n_het", models.IntegerField()),
                ("eur_n_homalt", models.IntegerField()),
                ("eur_freq_homref", models.FloatField()),
                ("eur_freq_het", models.FloatField()),
                ("eur_freq_homalt", models.FloatField()),
                ("oth_an", models.IntegerField()),
                (
                    "oth_ac",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                (
                    "oth_af",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(), size=None
                    ),
                ),
                ("oth_n_bi_genos", models.IntegerField()),
                ("oth_n_homref", models.IntegerField()),
                ("oth_n_het", models.IntegerField()),
                ("oth_n_homalt", models.IntegerField()),
                ("oth_freq_homref", models.FloatField()),
                ("oth_freq_het", models.FloatField()),
                ("oth_freq_homalt", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="ThousandGenomesSv",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("release", models.CharField(max_length=32)),
                ("chromosome", models.CharField(max_length=32)),
                ("start", models.IntegerField()),
                ("end", models.IntegerField()),
                ("bin", models.IntegerField(default=0)),
                (
                    "containing_bins",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(), size=None
                    ),
                ),
                ("start_ci_left", models.IntegerField()),
                ("start_ci_right", models.IntegerField()),
                ("end_ci_left", models.IntegerField()),
                ("end_ci_right", models.IntegerField()),
                (
                    "sv_type",
                    models.CharField(
                        choices=[
                            ("CNV", "CNV"),
                            ("DEL_ALU", "DEL_ALU"),
                            ("DEL", "DEL"),
                            ("DEL_LINE1", "DEL_LINE1"),
                            ("DEL_SVA", "DEL_SVA"),
                            ("DUP", "DUP"),
                            ("ALU", "ALU"),
                            ("LINE1", "LINE1"),
                            ("INS", "INS"),
                            ("SVA", "SVA"),
                            ("INV", "INV"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "source_call_set",
                    models.CharField(
                        choices=[
                            ("ALU_umary", "ALU_umary"),
                            ("CINV_delly", "CINV_delly"),
                            ("DEL_pindel", "DEL_pindel"),
                            ("DEL_union", "DEL_union"),
                            ("DUP_delly", "DUP_delly"),
                            ("DUP_gs", "DUP_gs"),
                            ("DUP_uwash", "DUP_uwash"),
                            ("INV_delly", "INV_delly"),
                            ("L1_umary", "L1_umary"),
                            ("NUMT_umich", "NUMT_umich"),
                            ("SVA_umary", "SVA_umary"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "mobile_element_info",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=32, null=True),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("num_samples", models.IntegerField()),
                ("num_alleles", models.IntegerField()),
                ("num_var_alleles", models.IntegerField()),
                ("num_alleles_afr", models.IntegerField()),
                ("num_var_alleles_afr", models.IntegerField()),
                ("num_alleles_amr", models.IntegerField()),
                ("num_var_alleles_amr", models.IntegerField()),
                ("num_alleles_eas", models.IntegerField()),
                ("num_var_alleles_eas", models.IntegerField()),
                ("num_alleles_eur", models.IntegerField()),
                ("num_var_alleles_eur", models.IntegerField()),
                ("num_alleles_sas", models.IntegerField()),
                ("num_var_alleles_sas", models.IntegerField()),
            ],
        ),
        migrations.AddIndex(
            model_name="thousandgenomessv",
            index=models.Index(
                fields=["release", "chromosome", "bin"], name="svdbs_thous_release_fadfda_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="gnomadsv",
            index=models.Index(
                fields=["release", "chromosome", "bin"], name="svdbs_gnoma_release_b9bf46_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="exaccnv",
            index=models.Index(
                fields=["release", "chromosome", "bin"], name="svdbs_exacc_release_c8af19_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dgvsvs",
            index=models.Index(
                fields=["release", "chromosome", "bin"], name="svdbs_dgvsv_release_2fc196_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dgvgoldstandardsvs",
            index=models.Index(
                fields=["release", "chromosome", "bin"], name="svdbs_dgvgo_release_a7129f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dbvarsv",
            index=models.Index(
                fields=["release", "chromosome", "bin"], name="svdbs_dbvar_release_72ea5e_idx"
            ),
        ),
    ]
